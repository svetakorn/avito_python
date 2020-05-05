from what_is_year_now import what_is_year_now
import unittest
from unittest.mock import patch
from io import StringIO


class TestWhatIsYearNow(unittest.TestCase):

    @patch('urllib.request.urlopen',
           return_value=StringIO('{"currentDateTime": "2019 05 03T21:04Z"}'))
    def test_format_wrong(self, arg):
        with self.assertRaises(ValueError):
            what_is_year_now()

    @patch('urllib.request.urlopen',
           return_value=StringIO('{"currentDateTime": "2019-05-03T21:04Z"}'))
    def test_format_1(self, arg):
        self.assertEqual(what_is_year_now(), 2019)

    @patch('urllib.request.urlopen',
           return_value=StringIO('{"currentDateTime": "03.05.2019T21:04Z"}'))
    def test_format_2(self, arg):
        self.assertEqual(what_is_year_now(), 2019)
