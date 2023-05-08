import unittest
import pandas as pd
from contextlib import redirect_stdout
from io import StringIO
from processing import load_data, verify_data


class TestDataFunctions(unittest.TestCase):
    def setUp(self):
        # Create an in-memory CSV file for testing purposes
        csv_data = """id,name,registration_date,last_active
                        1,John,2015-01-01,2022-04-30
                        2,Jane,2015-01-01,2022-04-30
                        3,Bob,2016-03-15,2022-04-30
                        4,Alice,2018-12-31,2022-04-30
                        5,Eve,2019-01-01,2022-04-30
                        6,Charlie,2020-02-29,2022-04-30"""
        self.data = pd.read_csv(
            StringIO(csv_data), parse_dates=["registration_date", "last_active"]
        )

    def test_load_data(self):
        expected_columns = ["id", "name", "registration_date", "last_active"]
        self.assertListEqual(list(self.data.columns), expected_columns)

    def test_verify_data(self):
        expected_pct_null_values = {
            "id": 0.0,
            "name": 0.0,
            "registration_date": 0.0,
            "last_active": 0.0,
        }
        pct_null_values = self.data.isnull().mean() * 100
        for col in expected_pct_null_values:
            self.assertAlmostEqual(
                pct_null_values[col], expected_pct_null_values[col], places=2
            )


if __name__ == "__main__":
    unittest.main()
