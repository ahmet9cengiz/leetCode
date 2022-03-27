class Solution(object):

    # Assuming len(strs) = n & len(strs[i]) = m
    # Time Complexity: O( n * min(m) ) = O(n*m)
    @staticmethod
    def longest_common_prefix(strs):
        prefix = ""
        i = 0
        keep_going = True

        while keep_going:
            current_letter = ''
            for s in strs:
                if i < len(s):
                    if current_letter == '':
                        current_letter = s[i]
                    else:
                        if current_letter != s[i]:
                            return prefix
                else:
                    return prefix

            prefix += current_letter
            i += 1

if __name__ == '__main__':
    s = Solution()
