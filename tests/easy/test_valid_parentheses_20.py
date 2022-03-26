from src.easy import valid_parentheses_20


def test_valid_parentheses():
    s = valid_parentheses_20.Solution()
    assert s.valid_parentheses("()[]{}") is True
    assert s.valid_parentheses("({[]})") is True
    assert s.valid_parentheses("{[}]()") is False