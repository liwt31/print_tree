# -*- coding: utf-8 -*-
# liwt31@163.com

import random

from colorama import init
from termcolor import colored

from tree import SearchTree

from print_tree import print_tree, PlaceHolder

init()


class print_binary(print_tree):
    def get_children(self, node):
        l_child, r_child = node.children
        if r_child is None and l_child is None:
            return []
        else:
            r_child = r_child or PlaceHolder
            l_child = l_child or PlaceHolder
            return [r_child, l_child]

    def get_node_str(self, node):
        raw_str = str(node.values[0])
        if node.values[0] % 2:
            return colored(raw_str, 'yellow')
        else:
            return colored(raw_str, 'cyan')


class print_binary_without_placeholder(print_binary):
    def get_children(self, node):
        l_child, r_child = node.children
        children = []
        if r_child is not None:
            children.append(r_child)
        if l_child is not None:
            children.append(l_child)
        return children


class print_tertiary(print_tree):
    def get_children(self, node):
        l_child, m_child, r_child = node.children
        if r_child is None and m_child is None and l_child is None:
            return []
        else:
            r_child = r_child or PlaceHolder
            m_child = m_child or PlaceHolder
            l_child = l_child or PlaceHolder
            return [r_child, m_child, l_child]

    def get_node_str(self, node):
        if node.full:
            return "{}, {}".format(*node.values)
        else:
            return "{}".format(node.values[0])


if __name__ == '__main__':
    elem_list = list(range(20))
    random.shuffle(elem_list)
    print("Insertion sequence: {}".format(elem_list))
    bst = SearchTree(elem_list)
    print_binary(bst.root)
    print_binary_without_placeholder(bst.root)
    tst = SearchTree(elem_list, 3)
    print_tertiary(tst.root)
