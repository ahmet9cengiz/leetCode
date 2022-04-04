class Solution(object):

    # Time Complexity: O(n)
    @staticmethod
    def maximum_subarray(nums):
        max_sum = nums[0]
        sums = [0 for _ in range(len(nums))]
        sums[0] = nums[0]

        for i in range(1,len(nums)):
            sums[i] = max(nums[i], sums[i-1]+nums[i])
            if sums[i] > max_sum:
                max_sum = sums[i]

        return max_sum

if __name__ == '__main__':
    s = Solution()
    print(s.maximum_subarray([-2,1,-3,4,-1,2,1,-5,4]))
