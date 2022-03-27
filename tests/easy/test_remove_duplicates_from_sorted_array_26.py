from src.easy import remove_duplicates_from_sorted_array_26


def test_remove_duplicates_from_sorted_array():
    s = remove_duplicates_from_sorted_array_26.Solution()

    expected = [1,2]
    nums = [1,1,2]
    k = s.remove_duplicates_from_sorted_array(nums)

    for i in range(k):
        assert nums[i] == expected[i]


