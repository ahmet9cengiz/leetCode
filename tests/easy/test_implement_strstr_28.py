from src.easy import implement_strstr_28


def test_implement_strstr():
    s = implement_strstr_28.Solution()
    assert s.implement_strstr("hello", "hel") == 0
    assert s.implement_strstr("hello", "") == 0
    assert s.implement_strstr("hello", "ell") == 1
    assert s.implement_strstr("hello", "llo") == 2
    assert s.implement_strstr("hello", "ella") == -1
