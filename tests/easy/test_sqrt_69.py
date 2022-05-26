from src.easy import sqrt_69


def test_sqrt():
    s = sqrt_69.Solution()
    assert s.sqrt(8) == 2
    assert s.sqrt(17) == 4
    assert s.sqrt(9) == 3
