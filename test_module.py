import unittest
from demographic_data_analyzer import calculate_demographic_data


class DemographicAnalyzerTestCase(unittest.TestCase):

    def test_calculate_demographic_data(self):
        data = calculate_demographic_data(print_data=False)

        self.assertEqual(
            data["race_count"]["White"], 27816
        )
        self.assertAlmostEqual(
            data["average_age_men"], 39.4
        )
        self.assertAlmostEqual(
            data["percentage_bachelors"], 16.4
        )
        self.assertAlmostEqual(
            data["higher_education_rich"], 46.5
        )
        self.assertAlmostEqual(
            data["lower_education_rich"], 17.4
        )
        self.assertEqual(
            data["min_work_hours"], 1
        )
        self.assertAlmostEqual(
            data["rich_percentage"], 10.0
        )
        self.assertEqual(
            data["highest_earning_country"], "Iran"
        )
        self.assertAlmostEqual(
            data["highest_earning_country_percentage"], 41.9
        )
        self.assertEqual(
            data["top_IN_occupation"], "Prof-specialty"
        )


def test_calculate_demographic_data():
    unittest.main(argv=[''], exit=False)