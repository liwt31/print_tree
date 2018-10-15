# -*- coding: utf-8 -*-
# liwt31@163.com

import random

from tree import SearchTree
from print_tree import print_tree


class Node(object):

    def __init__(self, value, parent):
        self.value = value
        self.children = []
        if parent is not None:
            parent.children.append(self)


class print_custom_tree(print_tree):

    def get_children(self, node):
        return node.children

    def get_node_str(self, node):
        return str(node.value)


class print_binary(print_tree):
    def get_children(self, node):
        l_child, r_child = node.children
        if r_child is None and l_child is None:
            return []
        else:
            return [r_child, l_child]

    def get_node_str(self, node):
        return str(node.values[0])


class print_binary_without_placeholder(print_tree):
    def get_children(self, node):
        l_child, r_child = node.children
        children = []
        if r_child is not None:
            children.append(r_child)
        if l_child is not None:
            children.append(l_child)
        return children

    def get_node_str(self, node):
        return str(node.values[0])


class print_tertiary(print_tree):
    def get_children(self, node):
        l_child, m_child, r_child = node.children
        if r_child is None and m_child is None and l_child is None:
            return []
        else:
            return [r_child, m_child, l_child]

    def get_node_str(self, node):
        if node.full:
            return '{}, {}'.format(*node.values)
        else:
            return '{}'.format(node.values[0])


if __name__ == '__main__':
    data_structure = Node('Data Stucture', None)

    vector = Node('Vector', data_structure)
    list_ = Node('List', data_structure)
    tree = Node('Tree', data_structure)
    graph = Node('Graph', data_structure)

    dag = Node('DAG', graph)
    avl = Node('AVL', tree)
    splay = Node('Splay', tree)
    b = Node('B', tree)
    quad = Node('Quand', tree)
    kd = Node('kd', tree)

    print_custom_tree(data_structure)

    elem_list = list(range(20))
    random.shuffle(elem_list)
    print(elem_list)
    bst = SearchTree(elem_list)
    print_binary(bst.root)
    print_binary_without_placeholder(bst.root)
    tst = SearchTree(elem_list, 3)
    print_tertiary(tst.root)
