from src.easy import palindrome_number_9


def test_palindrome_number():
    s = palindrome_number_9.Solution()
    assert s.palindrome_number(121) is True
    assert s.palindrome_number(-121) is False
    assert s.palindrome_number(128721) is False
