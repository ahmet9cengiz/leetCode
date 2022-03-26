class Solution(object):

    # Time Complexity: O(n)
    @staticmethod
    def palindrome_number(x):
        if x < 0:
            return False

        x = str(x)
        left_index = 0
        right_index = len(x) - 1

        while left_index < right_index:
            if x[left_index] != x[right_index]:
                return False
            else:
                left_index += 1
                right_index -= 1

        return True
