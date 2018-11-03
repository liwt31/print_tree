# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from colorama import init
from termcolor import colored

from .utils import Node, test_print_tree, get_complete_binary_tree

init()


class print_color_tree(test_print_tree):
    def get_node_str(self, node):
        orig_str = super(print_color_tree, self).get_node_str(node)
        return colored(orig_str, "green", "on_red")


def test_color_tree():
    expected = [
        " \u2001 \u2001 ┌\x1b[41m\x1b[32m0\x1b[0m",
        " \u2001 ┌\x1b[41m\x1b[32m0\x1b[0m┤",
        " \u2001 │ └\x1b[41m\x1b[32m0\x1b[0m",
        " ┌\x1b[41m\x1b[32m0\x1b[0m┤",
        " │ │ ┌\x1b[41m\x1b[32m0\x1b[0m",
        " │ └\x1b[41m\x1b[32m0\x1b[0m┤",
        " │ \u2001 └\x1b[41m\x1b[32m0\x1b[0m",
        "\x1b[41m\x1b[32m0\x1b[0m┤",
        " │ \u2001 ┌\x1b[41m\x1b[32m0\x1b[0m",
        " │ ┌\x1b[41m\x1b[32m0\x1b[0m┤",
        " │ │ └\x1b[41m\x1b[32m0\x1b[0m",
        " └\x1b[41m\x1b[32m0\x1b[0m┤",
        " \u2001 │ ┌\x1b[41m\x1b[32m0\x1b[0m",
        " \u2001 └\x1b[41m\x1b[32m0\x1b[0m┤",
        " \u2001 \u2001 └\x1b[41m\x1b[32m0\x1b[0m",
    ]
    root = get_complete_binary_tree(3)
    p = print_color_tree(root)
    for row1, row2 in zip(expected, p.rows):
        assert row1 == row2


def test_wide_character_tree():
    expected = [
        "    \u2001    \u2001    ┌哈哈",
        "    \u2001    ┌哈哈┤",
        "    \u2001    │    └哈哈",
        "    ┌哈哈┤",
        "    │    │    ┌哈哈",
        "    │    └哈哈┤",
        "    │    \u2001    └哈哈",
        "哈哈┤",
        "    │    \u2001    ┌哈哈",
        "    │    ┌哈哈┤",
        "    │    │    └哈哈",
        "    └哈哈┤",
        "    \u2001    │    ┌哈哈",
        "    \u2001    └哈哈┤",
        "    \u2001    \u2001    └哈哈",
    ]
    root = get_complete_binary_tree(3, "哈哈")
    p = test_print_tree(root)
    print([repr(row) for row in p.rows])
    for row1, row2 in zip(expected, p.rows):
        assert row1 == row2
