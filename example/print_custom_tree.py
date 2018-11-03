# -*- coding: utf-8 -*-
# liwt31@163.com

from colorama import init
from termcolor import colored

from print_tree import print_tree

init()


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

if __name__ == "__main__":
    data_structure = Node(colored("Data Stucture", 'blue', 'on_white'), None)

    vector = Node(colored("Vector", 'cyan'), data_structure)
    list_ = Node(colored("List", 'cyan'), data_structure)
    tree = Node(colored("Tree", 'cyan'), data_structure)
    graph = Node(colored("Graph", 'cyan'), data_structure)

    dag = Node(colored("DAG", 'magenta'), graph)
    avl = Node(colored("AVL", 'magenta', attrs=['bold']), tree)
    splay = Node(colored("Splay", 'magenta', attrs=['underline']), tree)
    b = Node(colored("B", 'magenta', attrs=['dark']), tree)
    quad = Node(colored("Quand", 'magenta', attrs=['blink']), tree)
    kd = Node(colored("kd", attrs=['concealed']), tree)

    print_custom_tree(data_structure)

