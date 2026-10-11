"""Nonclinical arithmetic tests with contrived aggregate counts; no patient data."""
import unittest

from scripts.paired_binary_summary import (
    exact_mcnemar_p_value,
    paired_summary,
    wilson_interval,
)


class PairedPlanningTests(unittest.TestCase):
    def test_perfect_agreement_has_no_discordance(self):
        result = paired_summary(9, 0, 0, 1)
        self.assertEqual(result["episode_count"], 10)
        self.assertEqual(result["discordant_episode_count"], 0)
        self.assertEqual(result["exact_two_sided_mcnemar_p_value"], 1.0)

    def test_one_sided_discordance_exact_value(self):
        self.assertAlmostEqual(exact_mcnemar_p_value(0, 10), 2 / 1024)

    def test_discordance_symmetry(self):
        self.assertAlmostEqual(
            exact_mcnemar_p_value(2, 7),
            exact_mcnemar_p_value(7, 2),
        )

    def test_balanced_discordance_is_not_significant(self):
        self.assertEqual(exact_mcnemar_p_value(10, 10), 1.0)

    def test_larger_llm_error_rate_positive_delta(self):
        result = paired_summary(80, 2, 8, 10)
        self.assertEqual(result["episode_count"], 100)
        self.assertAlmostEqual(result["rule_critical_error_rate"], 0.12)
        self.assertAlmostEqual(result["llm_critical_error_rate"], 0.18)
        self.assertAlmostEqual(result["llm_minus_rule_rate_difference"], 0.06)

    def test_wilson_zero_events_never_claims_zero_upper_limit(self):
        lo, hi = wilson_interval(0, 100)
        self.assertEqual(lo, 0.0)
        self.assertGreater(hi, 0.0)

    def test_wilson_all_events_reaches_one(self):
        lo, hi = wilson_interval(100, 100)
        self.assertLess(lo, 1.0)
        self.assertEqual(hi, 1.0)

    def test_invalid_negative_counts_rejected(self):
        with self.assertRaises(ValueError):
            paired_summary(10, -1, 0, 0)
        with self.assertRaises(ValueError):
            exact_mcnemar_p_value(-1, 0)

    def test_zero_total_rejected(self):
        with self.assertRaises(ValueError):
            paired_summary(0, 0, 0, 0)

    def test_noninteger_counts_rejected(self):
        with self.assertRaises(TypeError):
            paired_summary(10, 0.5, 0, 0)

    def test_wilson_invalid_n_rejected(self):
        with self.assertRaises(ValueError):
            wilson_interval(1, 0)


if __name__ == "__main__":
    unittest.main()
