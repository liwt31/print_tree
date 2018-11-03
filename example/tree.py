# -*- coding: utf-8 -*-
# liwt31@163.com


class Node(object):
    def __init__(self, value, branch):
        self.values = [value]
        self.branch = branch
        self.children = [None] * branch

    def add_child(self, value):
        if not self.full:
            self.values.append(value)
            self.values.sort()
            return self
        new_node = Node(value, self.branch)
        for idx, self_value in enumerate(self.values):
            if value <= self_value:
                self.children[idx] = new_node
                return new_node
        self.children[-1] = new_node
        return new_node

    @property
    def full(self):
        return len(self.values) == self.branch - 1


class SearchTree(object):
    def __init__(self, sequence, branch=2):
        if len(sequence) == 0:
            return
        self.root = Node(sequence[0], branch)
        for value in sequence[1:]:
            self.insert(value)

    def insert(self, value, node=None):
        node = node or self.root
        if node.full:
            for idx, node_value in enumerate(node.values):
                if value <= node_value:
                    child = node.children[idx]
                    break
            else:
                child = node.children[-1]
            if child is None:
                return node.add_child(value)
            else:
                return self.insert(value, child)
        else:
            return node.add_child(value)
