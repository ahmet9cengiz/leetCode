class Solution(object):

    # Time Complexity: O(n)
    @staticmethod
    def climbing_stairs(n):
        cur_step = 1  # first step
        prev_step = 1  # 0th step
        next_step = 2  #second step

        # fibonacci
        for i in range(n-1):
            next_step = cur_step + prev_step
            prev_step = cur_step
            cur_step = next_step
        
        return cur_step



if __name__ == '__main__':
    s = Solution()
    print(s.climbing_stairs(2))
