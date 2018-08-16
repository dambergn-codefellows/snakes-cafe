from snakes_cafe import test
from snakes_cafe import list_category
import sys
# import pytest
# lookup standard out / standard in


def test_test_module_exists():
    assert test() is True


def test_list_category(capsys):
    actual = list_category('appetizers')
    captured = capsys.captured.out
    print('captured: ', capsys.captured.out)
    assert captured == actual
# def test_list_gets_reversed():
#     expected = [1, 2, 3, 4]
#     actual = reverse_array([4, 3, 2, 1])
#     assert expected == actual