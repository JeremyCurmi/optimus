import pytest
from src.api.discord import extract_username_from_name


def test_extract_username_from_name():
    test_cases = {'var': 'jeremy01#101', 'expected': 'jeremy01'}
    for test in test_cases:
        got = extract_username_from_name(test['var'])
        assert got == test['expected']
