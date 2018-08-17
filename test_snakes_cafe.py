from snakes_cafe import greeting, list_category, message, manual, exit, complete, add_menue_item, remove_menue_item
import sys
# import pytest
# lookup standard out / standard in


def test_greeting_exists():
    assert greeting


def test_list_category_exists():
    assert list_category


def test_message_exists():
    assert message


def test_manual_exists():
    assert manual


def test_exit_exists():
    assert exit


def test_complete_exists():
    assert complete


def test_add_menue_item_exists():
    assert add_menue_item


def test_remove_menue_item_exists():
    assert remove_menue_item


# def test_list_category(capsys):
#     actual = list_category('appetizers')
#     expected = 'spinach artichoke dip'
#     # captured = capsys.captured.out
#     # print('captured: ', capsys.captured.out)
#     assert expected == actual

# def test_list_gets_reversed():
#     expected = [1, 2, 3, 4]
#     actual = reverse_array([4, 3, 2, 1])
#     assert expected == actual