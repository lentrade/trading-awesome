import contextlib
import io
import json
import sys
import unittest
from functools import partial
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import pr_guard  # noqa: E402
from test_trust import NOW, FakeGitHub  # noqa: E402

ENTRY = "name: Acme\nurl: {url}\ncategory: market-data\n"


class FakeRepoGitHub(FakeGitHub):
    def __init__(self, files, contents, **kw):
        super().__init__(**kw)
        self._files, self._contents = files, contents

    def pull_files(self, number):
        return self._files

    def file_at(self, repo, path, ref):
        return self._contents.get((ref, path))


def pr_event(author="contributor", body=""):
    return {"action": "opened", "pull_request": {
        "number": 7, "state": "open", "body": body, "author_association": "NONE",
        "user": {"login": author, "type": "User"},
        "head": {"sha": "head", "repo": {"full_name": "contributor/trading-awesome"}},
        "base": {"sha": "base"},
    }}


def run_guard(gh, event):
    buffer = io.StringIO()
    # Match FakeGitHub's fixed clock so account ages do not drift over time.
    fixed_assess = partial(pr_guard.assess, now=NOW)
    with contextlib.redirect_stdout(buffer), patch("pr_guard.assess", fixed_assess):
        pr_guard.run(event, gh, dry_run=True)
    return json.loads(buffer.getvalue())


class PrGuardTest(unittest.TestCase):
    def test_young_account_is_closed(self):
        gh = FakeRepoGitHub([{"filename": "FAQ.md", "status": "modified"}], {}, created_days_ago=10)
        result = run_guard(gh, pr_event())
        self.assertTrue(result["close"])
        self.assertIn("trust-check-failed", result["labels"])

    def test_first_timer_adding_entry_is_sent_to_form(self):
        files = [{"filename": "data/entries/acme.yml", "status": "added"}]
        contents = {("head", "data/entries/acme.yml"): ENTRY.format(url="https://acme.example/")}
        result = run_guard(FakeRepoGitHub(files, contents), pr_event())
        self.assertTrue(result["close"])
        self.assertIn("use-submission-form", result["labels"])

    def test_domain_change_is_labelled(self):
        files = [{"filename": "data/entries/acme.yml", "status": "modified"}]
        contents = {
            ("base", "data/entries/acme.yml"): ENTRY.format(url="https://acme.example/"),
            ("head", "data/entries/acme.yml"): ENTRY.format(url="https://acme-login.example/"),
        }
        result = run_guard(FakeRepoGitHub(files, contents), pr_event())
        self.assertFalse(result["close"])
        self.assertIn("domain-change", result["labels"])

    def test_referral_link_and_sensitive_files(self):
        files = [{"filename": "data/entries/acme.yml", "status": "modified"},
                 {"filename": ".github/workflows/ci.yml", "status": "modified"}]
        contents = {
            ("base", "data/entries/acme.yml"): ENTRY.format(url="https://acme.example/"),
            ("head", "data/entries/acme.yml"): ENTRY.format(url="https://acme.example/?ref=abc"),
        }
        result = run_guard(FakeRepoGitHub(files, contents), pr_event())
        self.assertTrue(any("tracking/referral" in p for p in result["problems"]))
        self.assertIn("sensitive-change", result["labels"])

    def test_affiliation_checkbox_labels_vendor(self):
        body = "- [x] I work for, own, or was paid or asked by a service changed here: Acme"
        gh = FakeRepoGitHub([{"filename": "FAQ.md", "status": "modified"}], {})
        self.assertIn("vendor-submitted", run_guard(gh, pr_event(body=body))["labels"])

    def test_unparseable_yaml_is_reported(self):
        files = [{"filename": "data/entries/acme.yml", "status": "modified"}]
        contents = {("head", "data/entries/acme.yml"): "name: [unclosed"}
        result = run_guard(FakeRepoGitHub(files, contents, merged=1), pr_event())
        self.assertTrue(any("not a valid entry" in p for p in result["problems"]))


if __name__ == "__main__":
    unittest.main()
