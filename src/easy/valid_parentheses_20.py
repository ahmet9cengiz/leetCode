class Solution(object):

    # Time Complexity: O(n)
    @staticmethod
    def valid_parentheses(s):
        parentheses_pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []

        for i in range(len(s)):

            if s[i] in parentheses_pairs:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                else:
                    last = stack[-1]
                    if parentheses_pairs[last] == s[i]:
                        stack.pop()
                    else:
                        return False

        if len(stack) == 0:
            return True
        else:
            return False
