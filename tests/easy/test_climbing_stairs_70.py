from src.easy import climbing_stairs_70


def test_climbing_stairs():
    s = climbing_stairs_70.Solution()
    assert s.climbing_stairs(2) == 2
    assert s.climbing_stairs(3) == 3
    assert s.climbing_stairs(5) == 8
