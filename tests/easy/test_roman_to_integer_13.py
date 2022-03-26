from src.easy import roman_to_integer_13


def test_roman_to_integer():
    s = roman_to_integer_13.Solution()
    assert s.roman_to_integer("III") == 3
    assert s.roman_to_integer("LVIII") == 58
    assert s.roman_to_integer("MCMXCIV") == 1994
