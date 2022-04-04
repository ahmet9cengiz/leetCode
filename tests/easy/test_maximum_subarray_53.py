from src.easy import maximum_subarray_53


def test_maximum_subarray():
    s = maximum_subarray_53.Solution()
    assert s.maximum_subarray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert s.maximum_subarray([1]) == 1
    assert s.maximum_subarray([5,4,-1,7,8]) == 23
    assert s.maximum_subarray([-5, -2]) == -2

