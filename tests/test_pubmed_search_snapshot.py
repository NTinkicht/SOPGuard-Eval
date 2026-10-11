"""Pure offline tests of PubMed metadata search logic. No network/patient data."""
import csv
import json
import tempfile
import unittest
from pathlib import Path
from scripts.pubmed_search_snapshot import search_one, run_snapshot, request_json


class PubMedQueryTests(unittest.TestCase):
    def test_count_pagination_and_completion(self):
        calls = []
        def fetch(params):
            calls.append(params["retstart"])
            first = params["retstart"]
            return {"count": "4", "idlist": [str(x) for x in range(first + 1, 5)],
                    "querytranslation": "MOCK VALID QUERY"}
        result = search_one("Q", "fake", fetch=fetch, pause=lambda _: None, limit=10)
        self.assertEqual(result["reported_count"], 4)
        self.assertEqual(result["pmids"], ["1", "2", "3", "4"])
        self.assertTrue(result["complete_pmid_export"])

    def test_truncation_is_explicit(self):
        def fetch(params):
            return {"count": "3000", "idlist": ["1", "2"], "querytranslation": "MOCK"}
        result = search_one("Q", "fake", fetch=fetch, pause=lambda _: None, limit=2)
        self.assertFalse(result["complete_pmid_export"])
        self.assertEqual(result["retrieved_count"], 2)
        self.assertEqual(result["reported_count"], 3000)

    def test_count_change_rejected(self):
        calls = 0
        def fetch(params):
            nonlocal calls
            calls += 1
            if calls == 1:
                return {"count": "300", "idlist": [str(i) for i in range(200)]}
            return {"count": "301", "idlist": [str(i) for i in range(200, 301)]}
        with self.assertRaises(RuntimeError):
            search_one("Q", "fake", fetch=fetch, pause=lambda _: None, limit=400)

    def test_duplicate_ids_rejected(self):
        def fetch(params):
            return {"count": "2", "idlist": ["111", "111"]}
        with self.assertRaises(RuntimeError):
            search_one("Q", "fake", fetch=fetch, pause=lambda _: None)

    def test_non_numeric_pmid_rejected(self):
        def fetch(params):
            return {"count": "1", "idlist": ["INJECTION"]}
        with self.assertRaises(ValueError):
            search_one("Q", "fake", fetch=fetch, pause=lambda _: None)

    def test_bad_limit_rejected(self):
        with self.assertRaises(ValueError):
            search_one("Q", "fake", fetch=lambda _: {}, limit=2001)

    def test_missing_results_rejected(self):
        with self.assertRaises(ValueError):
            search_one("Q", "fake", fetch=lambda _: {"count": "1"})

    def test_aggregate_export_no_patient_information(self):
        with tempfile.TemporaryDirectory() as folder:
            def fetch(params):
                return {"count": "2", "idlist": ["123", "456"],
                        "querytranslation": "MOCK"}
            manifest = run_snapshot(Path(folder), searches={"TEST": "fake"},
                                    fetch=fetch, pause=lambda _: None)
            self.assertEqual(manifest["results"][0]["reported_count"], 2)
            self.assertNotIn("pmids", manifest["results"][0])
            output = Path(folder)
            data = json.loads((output / "search_manifest.json").read_text())
            self.assertEqual(len(data["results"]), 1)
            with (output / "pmid_export.csv").open(newline="") as handle:
                self.assertEqual(list(csv.DictReader(handle)),
                                 [{"query_id": "TEST", "pmid": "123"},
                                  {"query_id": "TEST", "pmid": "456"}])


if __name__ == "__main__":
    unittest.main()
