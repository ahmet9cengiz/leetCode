import pytest
from src.easy import merge_two_sorted_lists_21 as q


def test_merge_two_sorted_lists():
    s = q.Solution()

    list1 = q.ListNode(1, q.ListNode(2, q.ListNode(4, None)))
    list2 = q.ListNode(1, q.ListNode(3, q.ListNode(4, None)))
    assert s.merge_two_sorted_lists(list1, list2) == q.ListNode(1, q.ListNode(1, q.ListNode
                                                                (2, q.ListNode(3, q.ListNode(4, q.ListNode(4, None))))))

    assert s.merge_two_sorted_lists(None, None) is None
    assert s.merge_two_sorted_lists(list1, None) == list1
    assert s.merge_two_sorted_lists(None, list2) == list2
