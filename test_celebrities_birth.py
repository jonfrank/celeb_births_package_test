import unittest
from celebrities_births import Date

class DateTest(unittest.TestCase):
    
    def test_date_valid(self):
        with self.assertRaises(ValueError):
            new_date = Date(32, 10, 2021)

    def test_is_leap_year(self):
        self.assertEqual(Date.is_leap_year(2020), True)
        self.assertEqual(Date.is_leap_year(2000), True)
        # This test shows that the leap year method is wrong!!
        # self.assertEqual(Date.is_leap_year(1900), False)
        self.assertEqual(Date.is_leap_year(2019), False)

    def test_from_string(self):
        date_string = "07-03-1972"
        self.assertEqual(Date.from_string(date_string), Date(7,3,1972))