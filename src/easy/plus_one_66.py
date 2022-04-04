class Solution(object):

    # Time Complexity: O(n)
    @staticmethod
    def plus_one(digits):
        keep_going = True
        for i, e in reversed(list(enumerate(digits))):
            if keep_going:
                if e == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    keep_going = False
            else:
                break

        if keep_going:
            new_digits = [1]
            new_digits[1:] = [digits[i] for i in range(len(digits))] 
            return new_digits

        return digits

if __name__ == '__main__':
    s = Solution()
    print(s.plus_one([9,9,9]))
