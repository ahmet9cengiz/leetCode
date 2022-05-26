from src.easy import remove_duplicates_from_sorted_list_83 as q


def test_remove_duplicates_from_sorted_list():
    s = q.Solution()
    assert s.remove_duplicates_from_sorted_list(q.ListNode(1, q.ListNode(2, q.ListNode(4, None)))) == q.ListNode(1, q.ListNode(2, q.ListNode(4, None)))
