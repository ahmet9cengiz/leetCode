class Solution(object):

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    @staticmethod
    def remove_element(nums, val):
        size = len(nums)
        j = size -1  # going backwards 
        i = 0

        while i <= j:
            if nums[i] == val:
                if nums[j] != val:
                    nums[i] = nums[j]
                    j -= 1
                    i += 1
                else:  
                    j -= 1
            else:
                i += 1

        return j+1

if __name__ == '__main__':
    s = Solution()
    val = 2
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
