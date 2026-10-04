# Attribution and modifications

SEOAGENT was created after reviewing the `local-seo-agent` repository supplied by Amar Pearson.

The original repository is copyright (c) 2026 Jono Catliff and distributed under the MIT License. The original project provided a useful command-oriented structure for Google Business Profile work, review workflows, keyword research, service pages, blog posts, publishing and quality checks.

This implementation is not a verbatim copy. It changes the operating model in several material ways:

- Google Search Console evidence is the first prioritization layer for existing sites.
- Existing pages are improved before new pages are created.
- Important queries receive explicit canonical page ownership.
- Cannibalization and accidental intent leakage are surfaced as first-class issues.
- Review requests do not gate access to Google Reviews based on rating or sentiment.
- Local/service pages require evidence of distinct user value; mass city/service generation is not the default.
- The system is platform-agnostic rather than dependent on Claude Code.
- Business facts are stored separately from reusable workflows.

See `LICENSE` for the original MIT license text.
