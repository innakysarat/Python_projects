import unittest
from typing import List

from one_hot_encoder import fit_transform


class TestFt(unittest.TestCase):
    def test_ft(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        actual = fit_transform(cities)
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]

        self.assertEqual(actual, expected)

        names = ['Misha', 'Stepan', 'Boris', 'Egor', 'Misha']
        actual = fit_transform(names)
        expected = [
            ('Misha', [0, 0, 0, 1]),
            ('Stepan', [0, 0, 1, 0]),
            ('Boris', [0, 1, 0, 0]),
            ('Egor', [1, 0, 0, 0]),
            ('Misha', [0, 0, 0, 1])
        ]
        unexpected = [
            ('Inna', [0, 0, 0, 1]),
            ('Stepan', [0, 0, 1, 0]),
            ('Boris', [0, 1, 0, 0]),
            ('Egor', [1, 0, 0, 0])
        ]
        self.assertEqual(actual, expected)
        self.assertNotEqual(actual, unexpected)
        self.assertFalse(len(actual) == 0)

    def test_tf_empty(self):
        actual = fit_transform([])
        self.assertTrue(len(actual) == 0)
        self.assertIsNotNone(actual)
        self.assertRaises(TypeError)

    def test_in(self):
        fruits: List[str] = ['Apple', 'Pear', 'Mandarin']
        actual = fit_transform(fruits)
        expected = ('Apple', [0, 0, 1])
        unexpected = ('Orange', [0, 0, 0])
        self.assertIn(expected, actual)
        self.assertNotIn(unexpected, actual)


if __name__ == '__main__':
    unittest.main()
