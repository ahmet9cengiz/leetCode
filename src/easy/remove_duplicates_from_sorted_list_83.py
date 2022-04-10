class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.next == other.next and self.val == other.val

class Solution(object):

    # Time Complexity: O(n)
    def remove_duplicates_from_sorted_list(self, head):
        root = head
        while head is not None:
            if head.next is None:
                break
            elif head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next         
        return root

if __name__ == '__main__':
    s = Solution()
    head = s.remove_duplicates_from_sorted_list(ListNode(1, ListNode(1, ListNode(1, None))))
    while head is not None:
        print(head.val)
        head = head.next