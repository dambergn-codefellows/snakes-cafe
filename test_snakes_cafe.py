from snakes_cafe import test
# import pytest
# lookup standard out / standard in


def test_test_module_exists():
    assert test() is True


# def test_list_gets_reversed():
#     expected = [1, 2, 3, 4]
#     actual = reverse_array([4, 3, 2, 1])
#     assert expected == actual