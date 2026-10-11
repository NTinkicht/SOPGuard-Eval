#!/usr/bin/env python3
"""Exploratory, NONCLINICAL paired binary error-count summary.

Consumes four aggregate counts only. Never accepts episode records, patient-level data,
SOP text, clinical measurements or model outputs. Not a sample-size calculator,
not a registered SAP, not valid for clustered/repeated observations as independent.
"""
from __future__ import annotations

import argparse
import json
import math
from statistics import NormalDist


def exact_mcnemar_p_value(rule_only: int, llm_only: int) -> float:
    """Two-sided exact conditional McNemar p for a single independent pair per case.

    Discordant counts: rule-only error, LLM-only error. Hypothesis: symmetric
    discordance. Does not account for multiple endpoints, clusters or repeats.
    """
    if not isinstance(rule_only, int) or not isinstance(llm_only, int):
        raise TypeError("Discordant counts must be integers")
    if rule_only < 0 or llm_only < 0:
        raise ValueError("Discordant counts cannot be negative")
    d = rule_only + llm_only
    if d == 0:
        return 1.0
    k = min(rule_only, llm_only)
    lower_tail = sum(math.comb(d, j) for j in range(k + 1)) / (2 ** d)
    return min(1.0, 2.0 * lower_tail)


def wilson_interval(events: int, total: int, confidence: float = 0.95) -> tuple[float, float]:
    """Unpaired binomial Wilson interval for ONE arm's descriptive event rate."""
    if not isinstance(events, int) or not isinstance(total, int):
        raise TypeError("Event and total counts must be integers")
    if not 0 <= events <= total or total <= 0:
        raise ValueError("Need 0 <= events <= total and total > 0")
    if not 0 < confidence < 1:
        raise ValueError("Confidence level must be between 0 and 1")
    z = NormalDist().inv_cdf((1 + confidence) / 2)
    p = events / total
    d = 1 + z * z / total
    center = (p + z * z / (2 * total)) / d
    half = z * math.sqrt((p * (1 - p) / total) + z * z / (4 * total * total)) / d
    return (max(0.0, center - half), min(1.0, center + half))


def paired_summary(neither: int, rule_only: int, llm_only: int, both: int) -> dict:
    """Summarize four synthetic/approved aggregate counts, never raw episode data."""
    vals = (neither, rule_only, llm_only, both)
    if any(not isinstance(x, int) for x in vals):
        raise TypeError("All four counts must be integers")
    if any(x < 0 for x in vals):
        raise ValueError("Counts cannot be negative")
    n = sum(vals)
    if n == 0:
        raise ValueError("At least one episode required")

    rule_events = rule_only + both
    llm_events = llm_only + both
    return {
        "episode_count": n,
        "rule_critical_error_count": rule_events,
        "llm_critical_error_count": llm_events,
        "rule_critical_error_rate": rule_events / n,
        "llm_critical_error_rate": llm_events / n,
        "llm_minus_rule_rate_difference": (llm_only - rule_only) / n,
        "rule_wilson_95_interval": wilson_interval(rule_events, n),
        "llm_wilson_95_interval": wilson_interval(llm_events, n),
        "discordant_episode_count": rule_only + llm_only,
        "exact_two_sided_mcnemar_p_value": exact_mcnemar_p_value(rule_only, llm_only),
        "limitations": (
            "Descriptive or exploratory only; one independent pair per episode. "
            "No matched difference CI, no power calculation, no clustering or "
            "stochastic-run adjustment, no multiple-testing correction. "
            "Not validated for clinical inference; independent expert labels required."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="NONCLINICAL paired S4 error summary from approved aggregate counts only"
    )
    for name in ("neither", "rule-only", "llm-only", "both"):
        parser.add_argument("--" + name, type=int, required=True)
    args = parser.parse_args()
    result = paired_summary(
        args.neither, args.rule_only, args.llm_only, args.both
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
