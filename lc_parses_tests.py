import pytest
from lc_parsers import  get_int_f, get_int_o

cases = [
    #Некоректні
    ("abc", None),
    ("1234abc", None),
    ('{"val": 10}', None),
    ('{"value": "10"}', None),
    ('{"value": null}', None),
    ('{"value": 12.5}', None),
    ('{"value": [1,2,3]}', None),
    ("", None),
    ("   ", None),
    ('{"value": true}', 1),
    ('{"value": "not a number"}', None),

    # Коректні строки
    ("0", 0),
    ("42", 42),
    ("000123", 123),
    ('{"value": 77}', 77),
    ('{"value": -5}', -5),
    ('{"value": 0}', 0),
    ("99999999999999999999", 99999999999999999999),
    ('{"value": 9999999999}', 9999999999),
]

def test_separator_o():
    print("\n\n========== STARTING OOP TESTS")
    assert  True

@pytest.mark.parametrize("input_str,expected", cases)
def test_get_int_o(input_str, expected):
    assert  get_int_o(input_str) == expected

def test_separator_f():
    print("\n\n========== STARTING FUNC TESTS")
    assert True

@pytest.mark.parametrize("input_str,expected", cases)
def test_get_int_f(input_str, expected):
    assert get_int_f(input_str) == expected