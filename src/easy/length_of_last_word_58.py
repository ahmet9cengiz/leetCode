class Solution(object):

    # Time Complexity: O(n)
    @staticmethod
    def length_of_last_word(s):
        current_len = 0
        word_ended = True

        for i in s:
            if i == ' ':
                word_ended = True
            else:
                if word_ended:
                    current_len = 0
                    word_ended = False
                current_len += 1

        return current_len


if __name__ == '__main__':
    s = Solution()
    print(s.length_of_last_word("Hello World"))
