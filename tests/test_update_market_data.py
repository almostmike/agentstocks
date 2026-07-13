import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "update_market_data.py"
SPEC = importlib.util.spec_from_file_location("update_market_data", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class MarketSnapshotTests(unittest.TestCase):
    def test_build_snapshot_marks_positions_and_benchmark(self):
        state = {
            "cash": 400,
            "positions": [
                {"ticker": "AAA", "shares": 2, "avg_cost": 90},
                {"ticker": "BBB", "shares": 4, "avg_cost": 45},
            ],
        }
        closes = {
            "AAA": {"2026-07-13": 100},
            "BBB": {"2026-07-13": 50},
            "SPY": {"2026-07-13": 110},
        }

        snapshot, history = MODULE.build_snapshot(
            state, closes, "2026-07-13", inception_spy=100
        )

        self.assertEqual(snapshot["portfolio"]["account_value"], 800)
        self.assertEqual(snapshot["portfolio"]["return_pct"], -20)
        self.assertEqual(snapshot["benchmark"]["return_pct"], 10)
        self.assertEqual(snapshot["positions"][0]["value"], 200)
        self.assertEqual(history["spy_adjusted_close"], 110)

    def test_latest_common_market_date_requires_all_symbols(self):
        closes = {
            "AAA": {"2026-07-10": 1, "2026-07-13": 2},
            "SPY": {"2026-07-10": 3},
        }
        self.assertEqual(MODULE.latest_common_market_date(closes), "2026-07-10")

    def test_baseline_spy_date_uses_recorded_prior_close(self):
        ledger = [{"date": "2026-07-13", "spy_close_date": "2026-07-10"}]
        self.assertEqual(MODULE.baseline_spy_date(ledger), "2026-07-10")

    def test_finalize_provisional_spy_only_changes_matching_session(self):
        ledger = [
            {
                "date": "2026-07-13",
                "spy_close": 1,
                "spy_close_status": "PROVISIONAL: pending",
                "spy_live_at_check": 2,
                "rationale": MODULE.PROVISIONAL_SPY_RATIONALE_TEXT,
            }
        ]
        changed = MODULE.finalize_provisional_spy(ledger, "2026-07-13", 752.12345)
        self.assertTrue(changed)
        self.assertEqual(ledger[0]["spy_close"], 752.1235)
        self.assertEqual(ledger[0]["spy_close_status"], "FINAL: automated adjusted close")
        self.assertEqual(ledger[0]["rationale"], MODULE.FINAL_SPY_RATIONALE_TEXT)
        self.assertNotIn("spy_live_at_check", ledger[0])


if __name__ == "__main__":
    unittest.main()
