class Solution(object):

    # Time Complexity: O(n)
    @staticmethod
    def roman_to_integer(s):
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        number = 0
        i = 0
        while i < len(s):
            if i == len(s)-1:   # since we check current and next character in each iteration
                number += values[s[i]]
                return number

            current_c = s[i]
            next_c = s[i+1]

            if values[current_c] >= values[next_c]:
                number += values[current_c]
            else:
                number += values[next_c]-values[current_c]
                i += 1

            i += 1

        return number
