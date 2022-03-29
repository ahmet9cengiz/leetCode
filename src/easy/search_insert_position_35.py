class Solution(object):

    # Time Complexity: O(logn)
    def search_insert_position(self, nums, target):
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        
        return self.binary_search(nums, 0, len(nums), target)

    def binary_search(self, nums, left_index, right_index, target): # [left_index - right_index)
        if target < nums[left_index]:
            return left_index
        elif target > nums[right_index-1]:
            return right_index

        mid_index = (right_index - left_index) // 2 + left_index
        
        if target == nums[mid_index]:
            return mid_index
        elif target < nums[mid_index]:
            return self.binary_search(nums, 0, mid_index, target)
        elif target > nums[mid_index]:
            return self.binary_search(nums, mid_index+1, right_index, target)
            


if __name__ == '__main__':
    s = Solution()
    print(s.search_insert_position([1,3,5,6], 7))
