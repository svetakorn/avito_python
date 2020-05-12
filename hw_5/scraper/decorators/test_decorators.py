from scraper.decorators.decorators import timer, memoize
import unittest
from unittest.mock import patch, ANY, MagicMock
from scraper.utils.test_utils import create_fake_timer


class TestTimer(unittest.TestCase):

    @patch('time.perf_counter', create_fake_timer())
    def test_proper_delta(self):
        """Правильно считается дельта по времени"""
        with patch('scraper.decorators.logger.logger.write_log') as m:
            timer(lambda: ())()

        m.assert_called_once_with(ANY, ANY, '2.000000')

    def test_func_with_exception(self):
        with self.assertRaises(IndexError):
            timer(lambda: [][0])()


class TestMemoize(unittest.TestCase):

    def test_func_executes_once(self):
        """Функция вызвана 1 раз для одного и того же набора параметров"""
        mock_fn = MagicMock(return_value=5)
        memoized_fn = memoize(mock_fn)

        memoized_fn(3)
        memoized_fn(3)

        self.assertEqual(mock_fn.call_count, 1)

        memoized_fn(4)

        self.assertEqual(mock_fn.call_count, 2)

    def test_equal_return(self):
        """Мемоизация возвращает одни и те же значения для одного набора параметров"""
        mock_fn = MagicMock(return_value=5)
        memoized_fn = memoize(mock_fn)

        value1 = memoized_fn(3)
        value2 = memoized_fn(3)

        self.assertEqual(value1, value2)

    def test_func_with_exception(self):
        with self.assertRaises(IndexError):
            memoize(lambda: [][0])()
