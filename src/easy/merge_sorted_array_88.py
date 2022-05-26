class Solution(object):

    # Time Complexity: O(n)
    @staticmethod
    def merge_sorted_array(nums1, m, nums2, n):
        
        i = m - 1 #index for nums1
        j = n - 1 #index for nums2
        t = m + n - 1 #index for all

        while j >= 0:
            if i >= 0 and nums2[j] < nums1[i]:
                nums1[t] = nums1[i]
                i = i - 1
            else:
                nums1[t] = nums2[j]
                j = j - 1

            t = t - 1




if __name__ == '__main__':
    s = Solution()
    nums1 = [5,6,7,0,0,0]
    nums2 = [1,2,3]
    s.merge_sorted_array(nums1, 3, nums2, 3)
    print(nums1)
