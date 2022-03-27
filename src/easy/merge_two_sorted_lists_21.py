from typing import Optional


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
    def merge_two_sorted_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (list1 is None) and (list2 is None):
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1

        if list1.val < list2.val:
            list1.next = self.merge_two_sorted_lists(list1.next, list2)
            return list1
        else:
            list2.next = self.merge_two_sorted_lists(list1, list2.next)
            return list2
