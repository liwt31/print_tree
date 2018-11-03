# -*- coding: utf-8 -*-
# liwt31@163.com
from __future__ import print_function, unicode_literals

import warnings
import unicodedata
import re

from .compat import CompatRecursionError


class PlaceHolder(object):
    pass


def split_children(children_list):
    up_list = []
    mid_child = PlaceHolder
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


def check_all_placeholder(children_list):
    for child in children_list:
        if child is not PlaceHolder:
            return False
    return True


ANSI_CSI_RE = re.compile(
    "\001?\033\\[((?:\\d|;)*)([a-zA-Z])\002?"
)  # Control Sequence Introducer
ANSI_OSC_RE = re.compile(
    "\001?\033\\]((?:.|;)*?)(\x07)\002?"
)  # Operating System Command


def get_term_len(string):
    """
    return the length of the string in terminal
    not completed. todo: windows color
    """
    string = ANSI_CSI_RE.sub("", string)
    string = ANSI_OSC_RE.sub("", string)
    len_ = 0
    for ch in string:
        if unicodedata.east_asian_width(ch) in "FWN":
            len_ += 2
        else:
            len_ += 1
    return len_


# Box drawing characters: https://en.wikipedia.org/wiki/Box-drawing_character
# Unicode spaces: http://jkorpela.fi/chars/spaces.html
SPACE = "\u2001"  # a corss-platform wide space


class PrintTree(object):
    def __init__(self, node, max_depth=50):
        recursion_error_flag = False
        try:
            self.rows, self.idx = self.get_print_rows(node, max_depth)
        except CompatRecursionError:
            recursion_error_flag = True  # a little trick to hide LONG traceback
        else:
            print()  # a blank line
            for row in self.rows:
                print(row)
        if recursion_error_flag:
            raise ValueError(
                "Maximum recursion depth met. Is there a loop in your tree?"
            )

    def get_children(self, node):
        raise NotImplementedError

    def get_node_str(self, node):
        return "{}".format(node)

    def add_prefix(self, child, child_space, c1, c2, c3, max_depth):
        if child is PlaceHolder:
            return ["{}".format(child_space)], 0
        child_print_rows, center_row_idx = self.get_print_rows(child, max_depth - 1)
        new_child_print_rows = []
        for row_idx, row in enumerate(child_print_rows):
            if row_idx < center_row_idx:
                shape = c1
            elif row_idx == center_row_idx:
                shape = c2
            else:
                shape = c3
            new_child_print_rows.append("{}{}{}".format(child_space, shape, row))
        return new_child_print_rows, center_row_idx

    def get_print_rows(self, node, max_depth):
        if node is PlaceHolder:
            return [""], 0
        if max_depth == 0:
            children_list = []
            warnings.warn("Maximum depth met, some children are ommited.")
        else:
            children_list = self.get_children(node)
        node_str = self.get_node_str(node)
        new_center_row = 0
        if len(children_list) == 0:
            return [node_str], new_center_row
        print_rows = []
        child_space = " " * get_term_len(node_str)
        up_list, mid_child, down_list = split_children(children_list)
        valid_up = not check_all_placeholder(up_list)
        valid_mid = mid_child is not PlaceHolder
        valid_down = not check_all_placeholder(down_list)
        for idx, child in enumerate(up_list):
            if idx == 0:
                new_child_print_rows, _ = self.add_prefix(
                    child, child_space, SPACE, "┌", "│", max_depth
                )
            else:
                new_child_print_rows, _ = self.add_prefix(
                    child, child_space, "│", "├", "│", max_depth
                )
            print_rows.extend(new_child_print_rows)
        if valid_mid:
            if valid_up:
                if valid_down:
                    new_child_print_rows, center_row_idx = self.add_prefix(
                        mid_child, child_space, "│", "┼", "│", max_depth
                    )
                else:
                    new_child_print_rows, center_row_idx = self.add_prefix(
                        mid_child, child_space, "│", "┴", SPACE, max_depth
                    )
            else:
                if valid_down:
                    new_child_print_rows, center_row_idx = self.add_prefix(
                        mid_child, child_space, SPACE, "┬", "│", max_depth
                    )
                else:
                    new_child_print_rows, center_row_idx = self.add_prefix(
                        mid_child, child_space, SPACE, "─", SPACE, max_depth
                    )
            center_row_tail = new_child_print_rows[center_row_idx][len(child_space) :]
            new_center_row = "{}{}".format(node_str, center_row_tail)
            new_child_print_rows[center_row_idx] = new_center_row
            print_rows.extend(new_child_print_rows)
        else:
            if valid_up:
                shape = "┤" if valid_down else "┘"
            else:
                shape = "┐" if valid_down else ""
            new_center_row = "{}{}".format(node_str, shape)
            print_rows.append(new_center_row)
        for idx, child in enumerate(down_list):
            if idx != len(down_list) - 1:
                new_child_print_rows, _ = self.add_prefix(
                    child, child_space, "│", "├", "│", max_depth
                )
            else:
                new_child_print_rows, _ = self.add_prefix(
                    child, child_space, "│", "└", " ", max_depth
                )
            print_rows.extend(new_child_print_rows)
        new_center_idx = print_rows.index(new_center_row)
        return print_rows, new_center_idx
