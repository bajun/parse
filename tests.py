import unittest

from collections import Counter

from main import get_data, parse_and_count


class GetDataTestCase(unittest.TestCase):
    def test_returned_type(self):
        res = get_data(1)
        self.assertIsInstance(res, Counter)

    def test_exception(self):
        try:
            get_data(100)
            self.assertTrue(True)
        except IOError:
            self.fail("IOError was raised!")


class ParseAndCountTestCase(unittest.TestCase):

    def test_text_returned(self):
        res = parse_and_count(10)
        self.assertIsInstance(res, str)


if __name__ == '__main__':
    unittest.main()
