from snakes_cafe import greeting, list_category, message, manual, exit, current_order, add_menue_item, remove_menue_item, select_menue, print_menue, load_custom_menue, get_menue
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


def test_current_order_exists():
    assert current_order


def test_add_menue_item_exists():
    assert add_menue_item

def test_get_menue_exists():
    assert get_menue

# def test_get_menue_object():
#     select_menue('./assets/menue_dinner.csv')
#     expected = (MENUE == object)
#     assert expected == True

def test_remove_menue_item_exists():
    assert remove_menue_item

def test_select_menue_exists():
    assert select_menue

def test_print_menue_exists():
    assert print_menue

def test_load_custom_menue_exists():
    assert load_custom_menue



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