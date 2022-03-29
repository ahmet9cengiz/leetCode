from src.easy import search_insert_position_35


def test_search_insert_position():
    s = search_insert_position_35.Solution()
    assert s.search_insert_position([1,3,5,6], 7) == 4
    assert s.search_insert_position([1,3,5,6], 5) == 2
    assert s.search_insert_position([1,3,5,6], 4) == 2
    assert s.search_insert_position([3,5,6,10], 1) == 0
