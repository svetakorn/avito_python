from fibonacci import fibonacci_iter, fibonacci
from fibonacci import get_generator_nth_element, memoize
import unittest
from unittest.mock import MagicMock
from itertools import islice
from random import randint


class TestMemoize(unittest.TestCase):

    def test_func_executes_once(self):
        """
        Функция вызвана 1 раз для одного
        и того же набора параметров
        """
        mock_fn = MagicMock(return_value=5)
        memoized_fn = memoize(mock_fn)

        memoized_fn(3)
        memoized_fn(3)

        self.assertEqual(mock_fn.call_count, 1)

        memoized_fn(4)

        self.assertEqual(mock_fn.call_count, 2)

    def test_equal_return(self):
        """
        Мемоизация возвращает одни и те же значения
        для одного набора параметров
        """
        mock_fn = MagicMock(return_value=5)
        memoized_fn = memoize(mock_fn)

        value1 = memoized_fn(3)
        value2 = memoized_fn(3)

        self.assertEqual(value1, value2)

    def test_func_with_exception(self):
        with self.assertRaises(IndexError):
            memoize(lambda: [][0])()


class TestFibonacciIter(unittest.TestCase):

    def test_fibonacci_iter_first_elements(self):
        """
        Первые значения соответствуют
        последовательности Фибоначчи
        """
        actual = list(islice(fibonacci_iter(), 15))
        expected = [
            0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377
        ]
        self.assertEqual(actual, expected)

    def test_fibonacci_iter_three_in_series(self):
        """
        Для любых последовательных 3 элементов a,b,c
        выполняется правило c = a + b
        """
        first_index = randint(50, 1000)
        fib_three_el = list(islice(
            fibonacci_iter(),
            first_index,
            first_index + 3)
        )

        self.assertEqual(sum(fib_three_el[:2]), fib_three_el[-1])


class TestFibonacci(unittest.TestCase):

    def test_fibonacci(self):
        actual = [fibonacci(6), fibonacci(20)]
        expected = [8, 6765]
        self.assertEqual(actual, expected)

    def test_fibonacci_error(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)


class TestGetGeneratorNthElement(unittest.TestCase):

    def test_get_generator_nth_element(self):
        self.assertEqual(
            get_generator_nth_element((i for i in range(10)), 3),
            list((i for i in range(10)))[3]
        )

    def test_get_generator_nth_element_error(self):
        with self.assertRaises(ValueError):
            get_generator_nth_element((i for i in range(100)), -1)
