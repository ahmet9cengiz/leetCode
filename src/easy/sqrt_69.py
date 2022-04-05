class Solution(object):
    
    def sqrt(self, x):
        l, r = 0, x
        while l <= r:
            m = (l + r) // 2
            if m * m <= x < (m + 1) * (m + 1):
                return m
            elif m * m > x:
                r = m - 1
            else:
                l = m + 1


if __name__ == '__main__':
    s = Solution()
    print(s.sqrt(17))
