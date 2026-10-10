#!/usr/bin/env python3
"""Static research-repository checks; NEVER reads clinical data or executes SOPs."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = [ROOT / "schemas" / "benchmark_episode.schema.json",
           ROOT / "schemas" / "research_output.schema.json",
           ROOT / "schemas" / "model_view.schema.json"]
errors = []
for path in SCHEMAS:
    try:
        obj = json.loads(path.read_text(encoding="utf-8"))
        assert obj.get("$schema") == "https://json-schema.org/draft/2020-12/schema"
        assert obj.get("type") == "object"
        assert obj.get("properties")
        assert obj.get("additionalProperties") is False
    except (OSError, ValueError, AssertionError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: invalid metadata schema: {exc}")

# The inference-time contract must not contain expert-only outcomes or post-action values.
try:
    model_view = json.loads((ROOT / "schemas" / "model_view.schema.json").read_text(encoding="utf-8"))
    forbidden = {"adjudication", "outcome_evidence", "action_taken", "repeat_results",
                 "reportability_label", "reliability", "allowed_actions"}
    exposed = set(model_view.get("properties", {}))
    if exposed & forbidden:
        errors.append(f"model_view.schema.json exposes reference-only fields: {sorted(exposed & forbidden)}")
except (OSError, ValueError) as exc:
    errors.append(f"model view firewall contract could not be checked: {exc}")

# Only local relative .md links; no network, copyrighted SOP crawling or patient data access.
link = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
for md in ROOT.rglob("*.md"):
    if ".git" in md.parts:
        continue
    for candidate in link.findall(md.read_text(encoding="utf-8")):
        if candidate.startswith(("http://", "https://", "#", "mailto:", "search-result://")):
            continue
        target = candidate.split("#", 1)[0].split("?", 1)[0].replace("%20", " ")
        if target and not (md.parent / target).resolve().is_file():
            errors.append(f"{md.relative_to(ROOT)}: missing relative link: {candidate}")
if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print(f"PASS: {len(SCHEMAS)} research metadata schemas parsed; local markdown links resolved.")
