from print_tree import print_tree


class Node(object):
    def __init__(self, value):
        self.value = value
        self.l_child = self.r_child = None


class test_print_tree(print_tree):
    def get_children(self, node):
        if not node.l_child and not node.r_child:
            return []
        elif not node.r_child:
            return [node.l_child]
        elif not node.l_child:
            return [node.r_child]
        else:
            return [node.l_child, node.r_child]

    def get_node_str(self, node):
        return u"{}".format(node.value)


def get_complete_binary_tree(levels, value=0):
    if levels == 0:
        return Node(value)
    node = Node(value)
    node.l_child = get_complete_binary_tree(levels - 1, value)
    node.r_child = get_complete_binary_tree(levels - 1, value)
    return node
