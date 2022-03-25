from src.easy import longest_common_prefix_14


def test_longest_common_prefix():
    s = longest_common_prefix_14.Solution()
    assert s.longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert s.longest_common_prefix(["dog", "racecar", "car"]) == ""
