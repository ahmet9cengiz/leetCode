class Solution(object):

    @staticmethod
    def two_sum(nums, target):
        remainders = {}

        for i in range(len(nums)):
            if nums[i] in remainders:
                return [remainders.get(nums[i]), i]
            else:
                remainders[target-nums[i]] = i

        raise Exception("No solution!")


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.two_sum([3, 2, 4], 6))
