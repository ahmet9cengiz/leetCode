from src.easy import plus_one_66


def test_plus_one():
    s = plus_one_66.Solution()
    assert s.plus_one([1,2,3]) == [1,2,4]
    assert s.plus_one([4,3,2,1]) == [4,3,2,2]
    assert s.plus_one([9,9,9]) == [1,0,0,0]
