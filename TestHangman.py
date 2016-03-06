from unittest import mock
from Hangman import update_board, next_game
from EvilHangman import make_key


def test_next_game():
    with mock.patch('builtins.input', side_effect=["Y", "y", "N", "t"]):
        assert next_game() == True
        assert next_game() == True
        assert next_game() == False
        assert next_game() == False


def test_update_board():
    assert update_board("G", "BAG", ["_", "A", "_"]) == ["_", "A", "G"]
    assert update_board("H", "BAG", ["_", "A", "_"]) == ["_", "A", "_"]


def test_make_key():
    assert make_key("HAPPY", "P") == "00110"
    assert make_key("SCHOOL", "K") == "000000"
    assert make_key("AAA", "A") == "111"
