class Solution(object):

    # Time Complexity: O(n)
    @staticmethod
    def two_sum(nums, target):
        remainders = {}

        for i in range(len(nums)):
            if nums[i] in remainders:
                return [remainders.get(nums[i]), i]
            else:
                remainders[target-nums[i]] = i

        raise Exception("No solution!")
