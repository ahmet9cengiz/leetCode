from src.easy import add_binary_67


def test_add_binary():
    s = add_binary_67.Solution()
    assert s.add_binary("11", "1") == "100"
    assert s.add_binary("1010", "1011") == "10101"
    assert s.add_binary("111", "1111") == "10110"
