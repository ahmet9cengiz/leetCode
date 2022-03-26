import pytest
from src.easy import two_sum_1


def test_two_sum():
    s = two_sum_1.Solution()
    assert s.two_sum([3, 2, 4], 6) == [1, 2]

    with pytest.raises(Exception):
        assert s.two_sum([1, 2, 3, 4, 11], 10)
