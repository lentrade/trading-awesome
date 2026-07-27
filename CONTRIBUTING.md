# Contributing to Trading Awesome

Thank you for considering a contribution! This guide explains how to propose additions, corrections, and improvements.

## What We Welcome

### ✅ Good additions

- **New services** with a public API, active open-source repository, or significant developer adoption
- **Pricing updates** with a verifiable source link
- **SDK links** for additional languages (Python, Go, PHP, JavaScript/TypeScript, Rust, C#, Java)
- **Corrections** to descriptions, coverage labels, or broken links
- **New sections** or sub-categories if justified by volume of relevant tools
- **Guides, tutorials, or case studies** that help users evaluate and compare services

### ❌ What we generally decline

- Affiliate links or referral codes
- Services with no public API and no open-source offering
- Abandoned projects (no commits in 12+ months, no responses to issues)
- Duplicate entries (use the most appropriate canonical URL)
- Trading strategies, signals, or "guaranteed return" claims

---

## How to Contribute

### Option 1: Pull Request (preferred)

1. **Fork** the repository
2. **Create a branch**: `git checkout -b add-service-name`
3. **Edit `README.md`** following the existing format (see template below)
4. **Update the reference links** section with your source
5. **Submit a PR** with a clear description

### Option 2: Open an Issue

If you're unsure about adding something, open an issue with:
- Service name and URL
- What it does (1–2 sentences)
- Why it belongs on this list
- Which section it fits into

---

## Entry Format Template

When adding a new service, use this structure:

```markdown
| Rank | **[Service Name](https://example.com/)** [N] | Brief description of what it does. | Markets / scope labels | [API docs](https://docs.example.com/) · Py: [official/community](https://github.com/...) · Go: [official/community](https://github.com/...) · PHP: [official/community](https://github.com/...) | Pricing description with source. |
```

### Field guidelines

| Field | Rules |
|-------|-------|
| **Rank** | Leave blank or suggest; the maintainer will assign based on editorial review |
| **Name** | Link to the official site. Use the brand's preferred capitalization |
| **Superscript [N]** | Add a new reference number. Do not reuse existing numbers |
| **Description** | One sentence. Be factual, not promotional |
| **Markets / scope** | Use the coverage labels from the "How to use this list" section |
| **API docs** | Link to public documentation. If no public API exists, write "No public API identified" |
| **Packages** | Only link to verified GitHub repositories. Mark `community` if not first-party |
| **Pricing** | Include the source (e.g., "see [official pricing](URL)"). Use "contact sales" only if no public price exists |

### Coverage labels (use exactly these)

- `Crypto — spot / on-chain / DeFi`
- `Crypto — derivatives`
- `Traditional markets`
- `Forex / FX`
- `Brokerage / execution`
- `Research / automation`

### Reference format

Add your reference at the bottom of the README in the "Reference links" section:

```markdown
[N] Service Name — [Official site](https://...) · [Documentation](https://...) · [Pricing](https://...)
```

---

## Editorial Criteria

Before adding a service, check that it meets at least **two** of these criteria:

1. **Public API** with documented endpoints
2. **Active open-source repository** (commits within 6 months, responsive maintainers)
3. **Significant developer adoption** (evidenced by GitHub stars, community packages, or forum activity)
4. **Distinctive specialization** (fills a gap not covered by existing entries)
5. **Broad market coverage** or **deep data quality**

### Maintenance threshold

Open-source libraries should have:
- At least one commit in the last 12 months
- Closed issues or responses within 30 days
- Up-to-date dependencies (no critical CVEs unaddressed)

---

## Updating Existing Entries

### Pricing changes

When updating a price, include:
- The new price or plan description
- A link to the source page
- The date you verified it

Example:
```markdown
| ... | Free tier; public paid plans start at **$99/month** (verified 2026-07-27); see [official pricing](https://...) | ... |
```

### Broken links

If you find a broken link, please verify whether:
- The URL has changed (update it)
- The service has shut down (remove it or mark as deprecated)
- The page is temporarily down (check with `curl -I` or similar)

### Deprecations

If a service is shutting down or has been acquired, open an issue or PR to:
- Mark it with ~~strikethrough~~ in the table
- Add a note: "[Deprecated / Acquired by X as of YYYY-MM]"
- Suggest a replacement if applicable

---

## Style Guide

### Language

- Write in **English** (U.S. spelling)
- Use sentence case for descriptions
- Avoid superlatives ("best," "fastest," "most powerful") — be factual
- Use "U.S." not "US" for the country

### Formatting

- Use `**bold**` for service names and prices
- Use `code` for API endpoints, package names, and technical terms
- Use `[N]` superscripts for references (sequential, no gaps)
- Keep table rows to a single line where possible

### Accessibility

- Always provide link text (no bare URLs)
- Ensure color is not the only way information is conveyed (use badges, labels)
- Use descriptive alt text for any images

---

## Review Process

1. **Automated checks**: CI runs link-checkers and markdown linting on PRs
2. **Editorial review**: A maintainer reviews for accuracy, relevance, and formatting
3. **Ranking assignment**: The maintainer assigns or adjusts the rank based on the criteria above
4. **Merge**: Once approved, the PR is merged and the list is updated

Typical review time: **3–7 days**.

---

## Code of Conduct

- Be respectful and constructive in all interactions
- Assume good faith
- Focus on the quality of information, not on competitive positioning
- Disclose any affiliations with services you propose

---

## Questions?

- For quick questions, open a [Discussion](https://github.com/lentrade/trading-awesome/discussions)
- For bug reports or link rot, open an [Issue](https://github.com/lentrade/trading-awesome/issues)
- For substantial additions, open a [Pull Request](https://github.com/lentrade/trading-awesome/pulls)

Thank you for helping make this list more useful for the trading and quant community!
