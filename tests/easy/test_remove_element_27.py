from src.easy import remove_element_27


def test_remove_element():
    s = remove_element_27.Solution()

    val = 2
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    expected = [0, 1, 4, 0, 3]

    k = s.remove_element(nums, val)
    assert k == len(expected);

    for i in range(len(expected)):
        assert nums[i] == expected[i]