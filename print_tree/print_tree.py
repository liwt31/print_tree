# -*- coding: utf-8 -*-

def split_children(children_list):
    up_list = []
    mid_child = None
    down_list = []
    mid_idx = len(children_list) // 2
    for idx, child in enumerate(children_list):
        if idx < mid_idx:
            up_list.append(child)
        elif len(children_list) % 2 == 1 and idx == mid_idx:
            mid_child = child
        else:
            down_list.append(child)
    return up_list, mid_child, down_list


def check_all_none_child(children_list):
    for child in children_list:
        if child is not None:
            return False
    return True


class PrintTree(object):

    def __init__(self, node):
        rows, idx = self.get_print_rows(node)
        for row in rows:
            print(row)

    def get_children(self, node):
        raise NotImplementedError

    def get_node_str(self, node):
        raise NotImplementedError

    def add_prefix(self, child, child_space, c1, c2, c3):
        if child is None:
            return ['{}'.format(child_space), 0]
        child_print_rows, center_row_idx = self.get_print_rows(child)
        new_child_print_rows = []
        for row_idx, row in enumerate(child_print_rows):
            if row_idx < center_row_idx:
                shape = c1
            elif row_idx == center_row_idx:
                shape = c2
            else:
                shape = c3
            new_child_print_rows.append('{}{}{}'.format(child_space, shape, row))
        return new_child_print_rows, center_row_idx

    def get_print_rows(self, node):
        if node is None:
            return [''], 0
        children_list = self.get_children(node)
        node_str = self.get_node_str(node)
        new_center_row = 0
        if len(children_list) == 0:
            return [node_str], new_center_row
        print_rows = []
        child_space = ' ' * len(node_str)
        up_list, mid_child, down_list = split_children(children_list)
        valid_up = not check_all_none_child(up_list)
        valid_mid = mid_child is not None
        valid_down = not check_all_none_child(down_list)
        for idx, child in enumerate(up_list):
            if idx == 0:
                new_child_print_rows, _ = self.add_prefix(child, child_space, '  ', '┌', '│')
            else:
                new_child_print_rows, _ = self.add_prefix(child, child_space, '│', '├', '│')
            print_rows.extend(new_child_print_rows)
        if valid_mid:
            if valid_up:
                if valid_down:
                    new_child_print_rows, center_row_idx = self.add_prefix(mid_child, child_space, '│', '┼', '│')
                else:
                    new_child_print_rows, center_row_idx = self.add_prefix(mid_child, child_space, '│', '┴', '  ')
            else:
                if valid_down:
                    new_child_print_rows, center_row_idx = self.add_prefix(mid_child, child_space, '  ', '┬', '│')
                else:
                    new_child_print_rows, center_row_idx = self.add_prefix(mid_child, child_space, '  ', '─', '  ')
            center_row_tail = new_child_print_rows[center_row_idx][len(child_space):]
            new_center_row = '{}{}'.format(node_str, center_row_tail)
            new_child_print_rows[center_row_idx] = new_center_row
            print_rows.extend(new_child_print_rows)
        else:
            if valid_up:
                shape = '┤' if valid_down else '┘'
            else:
                # valid_down must be True
                shape = '┐'
            new_center_row = '{}{}'.format(node_str, shape)
            print_rows.append(new_center_row)
        for idx, child in enumerate(down_list):
            if idx != len(down_list) - 1:
                new_child_print_rows, _ = self.add_prefix(child, child_space, '│', '├', '│')
            else:
                new_child_print_rows, _ = self.add_prefix(child, child_space, '│', '└', '  ')
            print_rows.extend(new_child_print_rows)
        new_center_idx = print_rows.index(new_center_row)
        return print_rows, new_center_idx

