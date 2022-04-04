class Solution(object):

    @staticmethod
    def add_binary(a, b):
        extra_digits = len(a) - len(b)
        
        if extra_digits >= 0:
            b = extra_digits*'0' + b
        else :
            a = -1*extra_digits*'0' + a


        a_rev = a[::-1]
        b_rev = b[::-1]
        result = ""
        remainder = 0

        for i in range(len(a_rev)):
            cur = int(a_rev[i]) + int(b_rev[i]) + remainder
            if cur < 2:
                result += str(cur)
                remainder = 0
            else:
                result += '0' if cur == 2 else '1'
                remainder = 1

        if remainder == 1:
            result += '1'

        return result[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.add_binary("1010", "1011"))
