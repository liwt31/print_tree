from print_tree.print_tree import split_children, check_all_placeholder, PlaceHolder


def test_split_children():
    children = [0, 1, 2, 3, 4]
    up_list, mid_child, down_list = split_children(children)
    assert up_list == [0, 1]
    assert mid_child == 2
    assert down_list == [3, 4]


def test_check_all_placeholder():
    assert check_all_placeholder([PlaceHolder] * 10)
    assert not check_all_placeholder([PlaceHolder] * 10 + [1])
