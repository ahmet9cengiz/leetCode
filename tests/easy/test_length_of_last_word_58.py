from src.easy import length_of_last_word_58


def test_length_of_last_word():
    s = length_of_last_word_58.Solution()
    assert s.length_of_last_word("Hello World") == 5
    assert s.length_of_last_word("   fly me   to   the moon  ") == 4
    assert s.length_of_last_word("luffy is still joyboy") == 6
