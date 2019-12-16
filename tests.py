import helpers
import main
import mock
import multiprocessing
import unittest

from collections import Counter


class GetDataTestCase(unittest.TestCase):
    def test_returned_type(self):
        res = main.get_data(1)
        self.assertIsInstance(res, Counter)

    def test_exception(self):
        try:
            main.get_data(100)
            self.assertTrue(True)
        except IOError:
            self.fail("IOError was raised!")


class ParseAndCountTestCase(unittest.TestCase):
    def setUp(self):
        self.fake_counter = Counter({"First": 10, "Second": 9, "Third": 15})

    @mock.patch('main.prepare_chunks')
    @mock.patch('main.get_data_wrapped')
    def test_counter_valid(self, get_data_wrapped, prepare_chunks):
        def mock_get_data(n):
            return self.fake_counter

        get_data_wrapped.side_effect = mock_get_data

        def mock_prepare_chunks(times, proc_num):
            return [1]
        prepare_chunks.side_effect = mock_prepare_chunks

        res = main.parse(1)
        self.assertEqual(res, [self.fake_counter])

    def test_counter_returned(self):
        res = main.parse(10)
        self.assertIsInstance(res, list)


if __name__ == '__main__':
    unittest.main()
