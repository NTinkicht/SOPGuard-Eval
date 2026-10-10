"""Tests for public research metadata contracts only.

All test values are synthetic placeholders, not CBC patient values.
No clinical decision, SOP interpretation, LLM inference or patient data processing.
"""
from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker, ValidationError

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"
CASE_ID = "DELIBERATELY-SYNTHETIC-NOT-A-PATIENT"


def load_schema(name: str):
    return json.loads((SCHEMA_DIR / name).read_text(encoding="utf-8"))


MODEL = load_schema("model_view.schema.json")
EPISODE = load_schema("benchmark_episode.schema.json")
OUTPUT = load_schema("research_output.schema.json")


def validator(schema):
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def synthetic_model_view():
    return {
        "episode_id": CASE_ID,
        "analyser": {"vendor": "FICTIONAL", "model": "TOY-NONCLINICAL", "software_version": "0"},
        "sop_descriptor": {"document_id": "FAKE-SOP", "revision": "X", "passage_ids": []},
        "source_measurements": [
            {"code": "TOY_SIGNAL", "raw_value": 1.0, "raw_unit": "arbitrary",
             "known_analyser_method": None}
        ],
        "flags": ["MOCK-FLAG"],
        "observations": [
            {"category": "SPECIMEN_OBSERVATION", "description": "Fictional placeholder, not a patient."}
        ],
        "not_for_clinical_use": True,
    }


def synthetic_episode():
    return {
        "episode_id": CASE_ID,
        "site_code": "FICTIONAL-SITE",
        "analyser": {"vendor": "FICTIONAL", "model": "TOY-NONCLINICAL", "software_version": "0"},
        "sop": {"document_id": "FAKE-SOP", "revision": "X"},
        "measurements": [
            {"code": "TOY_SIGNAL", "source_run": "FAKE-RUN", "raw_value": 1.0,
             "raw_unit": "arbitrary", "derivation": "UNDETERMINED", "reliability": "UNCERTAIN"}
        ],
        "evidence": [{"evidence_id": "E-FAKE", "category": "ORIGINAL_RUN"}],
        "adjudication": {
            "status": "UNRESOLVED",
            "allowed_actions": [],
            "required_abstention": True,
        },
    }


def synthetic_output():
    return {
        "episode_id": CASE_ID,
        "arm_id": "L0",
        "proposed_actions": ["ABSTAIN_INSUFFICIENT_EVIDENCE"],
        "evidence_refs": ["E-FAKE"],
        "required_verifications": [],
        "reason": "Fictional illustration of an output schema.",
        "not_for_clinical_use": True,
    }


class MetadataContractTests(unittest.TestCase):
    def test_all_three_json_schemas_are_valid_draft_2020_12(self):
        for schema in (MODEL, EPISODE, OUTPUT):
            with self.subTest(schema=schema["title"]):
                self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
                Draft202012Validator.check_schema(schema)

    def test_model_accepts_only_synthetic_toy_view(self):
        validator(MODEL).validate(synthetic_model_view())

    def test_restricted_episode_is_not_accepted_as_model_input(self):
        validator(EPISODE).validate(synthetic_episode())
        with self.assertRaises(ValidationError):
            validator(MODEL).validate(synthetic_episode())

    def test_adjudication_key_is_rejected_at_top_level(self):
        example = synthetic_model_view()
        example["adjudication"] = {"allowed_actions": ["NO_ACTION"]}
        with self.assertRaises(ValidationError):
            validator(MODEL).validate(example)

    def test_reliability_key_is_rejected_inside_measurements(self):
        example = synthetic_model_view()
        example["source_measurements"][0]["reliability"] = "TRUSTED"
        with self.assertRaises(ValidationError):
            validator(MODEL).validate(example)

    def test_reference_label_hidden_in_observation_object_is_rejected(self):
        example = synthetic_model_view()
        example["observations"][0]["correct_action"] = "NO_ACTION"
        with self.assertRaises(ValidationError):
            validator(MODEL).validate(example)

    def test_followup_measurement_is_rejected(self):
        example = synthetic_model_view()
        example["followup_measurements"] = [{"code": "TOY_SIGNAL", "raw_value": 2.0}]
        with self.assertRaises(ValidationError):
            validator(MODEL).validate(example)

    def test_excludes_clinical_use_false_or_missing(self):
        example = synthetic_model_view()
        example["not_for_clinical_use"] = False
        with self.assertRaises(ValidationError):
            validator(MODEL).validate(example)
        del example["not_for_clinical_use"]
        with self.assertRaises(ValidationError):
            validator(MODEL).validate(example)

    def test_output_forbids_reportable_placeholder(self):
        example = synthetic_output()
        example["provisional_research_values"] = [
            {"code": "TOY_SIGNAL", "value": 1.0, "unit": "arbitrary",
             "not_reportable": True, "input_refs": ["FAKE-RUN"]}
        ]
        validator(OUTPUT).validate(example)
        example["provisional_research_values"][0]["not_reportable"] = False
        with self.assertRaises(ValidationError):
            validator(OUTPUT).validate(example)

    def test_output_rejects_unknown_action_and_live_use(self):
        example = synthetic_output()
        validator(OUTPUT).validate(example)
        example["proposed_actions"] = ["RELEASE_PATIENT_RESULT"]
        with self.assertRaises(ValidationError):
            validator(OUTPUT).validate(example)
        example = synthetic_output()
        example["not_for_clinical_use"] = False
        with self.assertRaises(ValidationError):
            validator(OUTPUT).validate(example)

    def test_model_schema_contains_no_nested_answer_key_properties(self):
        forbidden = {
            "adjudication", "outcome_evidence", "action_taken", "repeat_results",
            "reportability_label", "reliability", "allowed_actions",
            "followup_measurements", "correct_action", "post_correction_result",
            "ground_truth", "required_abstention", "reportable_codes",
        }
        found = []

        def visit(value):
            if isinstance(value, dict):
                props = value.get("properties")
                if isinstance(props, dict):
                    found.extend(k for k in props if k in forbidden)
                for child in value.values():
                    visit(child)
            elif isinstance(value, list):
                for child in value:
                    visit(child)

        visit(MODEL)
        self.assertEqual([], found, "Model schema leaks reference-only field names")


if __name__ == "__main__":
    unittest.main()
