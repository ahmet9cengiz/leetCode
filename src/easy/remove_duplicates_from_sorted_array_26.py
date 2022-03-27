class Solution(object):

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    @staticmethod
    def remove_duplicates_from_sorted_array(nums):
        if not nums:
            return 
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                nums[slow+1] = nums[fast]
                slow += 1
            fast += 1
        return slow + 1
    
if __name__ == '__main__':
    s = Solution()
    s.remove_duplicates_from_sorted_array([1, 1, 2])