from one_hot_encoder import fit_transform


class TestFT:
    def test_fit_transform(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        actual = fit_transform(cities)
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]

        assert actual == expected

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
        assert actual == expected
        assert actual != unexpected
        assert len(actual) != 0
