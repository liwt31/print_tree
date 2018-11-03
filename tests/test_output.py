# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from .utils import test_print_tree, get_complete_binary_tree


def test_output():
    expected = """\
     ┌0
   ┌0┤
   │ └0
 ┌0┤
 │ │ ┌0
 │ └0┤
 │   └0
0┤
 │   ┌0
 │ ┌0┤
 │ │ └0
 └0┤
   │ ┌0
   └0┤
     └0
    """
    p = test_print_tree(get_complete_binary_tree(3))
    for row1, row2 in zip(expected.splitlines(), p.rows):
        assert row1 == row2
