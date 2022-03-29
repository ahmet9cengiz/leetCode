from asyncio import current_task
from multiprocessing.dummy import current_process


class Solution(object):

    # Time Complexity: O(n)
    @staticmethod
    def implement_strstr(haystack, needle):

        len_of_haystack = len(haystack)
        len_of_needle = len(needle)

        if len_of_needle == 0:
            return 0
        if len_of_haystack < len_of_needle:
            return -1
        
        for i in range(len_of_haystack - len_of_needle + 1):
            if haystack[i:i+len_of_needle] == needle:
                return i
        
        return -1


if __name__ == '__main__':
    s = Solution()
    s.implement_strstr("hello", "hel")
