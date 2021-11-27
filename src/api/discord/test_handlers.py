from .handlers import extract_username_from_name


def test_extract_username_from_name():
    test_cases = [{'var': 'jeremy01#101', 'expected': 'jeremy01'},
                  {'var': 'optimus#6081', 'expected': 'optimus'}]
    for test in test_cases:
        var = test['var']
        expected = test['expected']
        got = extract_username_from_name(var)
        assert got == expected
