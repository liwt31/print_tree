import sys

import pytest

from .utils import Node, test_print_tree


root = Node(-1)
limit = sys.getrecursionlimit()
node = root


for i in range(limit + 1):
    new_node = Node(i)
    node.l_child = new_node
    node = new_node


def test_maxrecursion():
    with pytest.raises(ValueError):
        test_print_tree(root, limit + 1)


def test_warn_max_depth():
    with pytest.warns(UserWarning):
        test_print_tree(root)
