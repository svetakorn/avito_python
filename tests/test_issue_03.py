from one_hot_encoder import fit_transform
import unittest


class TestFT(unittest.TestCase):

    def test_type_error(self):
        with self.assertRaises(TypeError):
            fit_transform(123)

    def test_no_arguments(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_full_output(self):
        test_list = ['banana', 'apple', 'banana', 'banana', 'orange']
        actual = fit_transform(test_list)
        expected = [
            ('banana', [0, 0, 1]),
            ('apple', [0, 1, 0]),
            ('banana', [0, 0, 1]),
            ('banana', [0, 0, 1]),
            ('orange', [1, 0, 0])
        ]
        self.assertEqual(actual, expected)

    def test_max_binary_value(self):
        test_list = ['banana', 'apple', 'banana', 'banana', 'orange']
        output = fit_transform(test_list)
        actual = max([i for l in output for i in l[1]]) == 1
        self.assertTrue(actual)


if __name__ == '__main__':
    unittest.main()
