from src.easy import merge_sorted_array_88


def test_merge_sorted_array():
    s = merge_sorted_array_88.Solution()
    nums1 = [5,6,7,0,0,0]
    nums2 = [1,2,3]
    s.merge_sorted_array(nums1, 3, nums2, 3)
    assert nums1 == [1,2,3,5,6,7]