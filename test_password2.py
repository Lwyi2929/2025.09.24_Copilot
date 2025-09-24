# test_password2.py
import pytest
from password2 import check_password_strength

def test_empty_password():
    assert check_password_strength("") == "弱"

def test_short_password():
    assert check_password_strength("Ab1!") == "弱"

def test_only_digits():
    assert check_password_strength("123456789") == "中"

def test_only_lowercase():
    assert check_password_strength("abcdefghij") == "中"

def test_only_uppercase():
    assert check_password_strength("ABCDEFGHIJ") == "中"

def test_only_special_chars():
    assert check_password_strength("!@#$%^&*()") == "中"

def test_digits_and_lowercase():
    assert check_password_strength("abc123456") == "中"

def test_digits_and_uppercase():
    assert check_password_strength("ABC123456") == "中"

def test_lowercase_and_uppercase():
    assert check_password_strength("Abcdefghi") == "中"

def test_digits_uppercase_lowercase():
    assert check_password_strength("Abcdef123") == "中"

def test_digits_uppercase_special():
    assert check_password_strength("ABC1234!@") == "中"

def test_lowercase_uppercase_special():
    assert check_password_strength("Abcdef!@#") == "中"

def test_digits_lowercase_special():
    assert check_password_strength("abc123!@#") == "中"

def test_strong_password():
    assert check_password_strength("Password123!") == "強"

def test_strong_all_criteria():
    assert check_password_strength("A1b2c3d4!") == "強"

def test_exactly_eight_chars():
    assert check_password_strength("Abc123!@") == "中"

def test_long_but_missing_criteria():
    assert check_password_strength("abcdefghijklmno") == "中"