# Security and health-data handling

**Research-use-only repository. No PHI/patient-level CBC datasets or private SOPs.**

- Do not upload any real patient record, direct identifier, accession number, linkage salt, proprietary analyser manual, restricted SOP, API key or credential.
- Do not use public issues, PR comments or CI logs to disclose sensitive clinical details; report them through the responsible institution's approved channel.
- Assume public Git history is permanent. Removing a commit does not revoke its copies.
- Cloud model calls involving human data require prior written data/ethics and provider approval; use an authorized restricted environment.
- CI, external analytics, automation and deployments must never have access to clinical records.
- If sensitive material is accidentally pushed, stop use, follow institutional incident response, revoke exposed credentials and obtain professional privacy/security support. Do not merely delete the file and declare incident resolved.

No clinical use, instrument or LIS write-back, interpretation for patient care, or automatic result authorization is permitted by this project.
