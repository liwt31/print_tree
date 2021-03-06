# print_tree
[![Build Status](https://travis-ci.org/liwt31/print_tree.svg?branch=master)](https://travis-ci.org/liwt31/print_tree)
[![PyPI version](https://badge.fury.io/py/print-tree2.svg)](https://badge.fury.io/py/print-tree2)

This package helps you to print your tree structure in a pretty format.


### Install
```
pip install print-tree2
```
I wish to use `print_tree` as the name but the package is already on pypi though it's not working.
To verify your installation, try:
```
git clone https://github.com/liwt31/print_tree.git
cd print_tree/
pytest
```

### Features
There is already a pretty print tree lib on GitHub [pptree](https://github.com/clemtoy/pptree), why reinvent another wheel?
The most important reason is:
* **This package provides an inherit interface that does not require you to modify any of your code**, while [pptree](https://github.com/clemtoy/pptree) by design requires your node class to have certain methods or properties.

Besides, this package:
* Does not change the order of your children ([pptree](https://github.com/clemtoy/pptree) does).
* Uses Unicode to achieve cross-platform -- [pptree](https://github.com/clemtoy/pptree) fails on Windows because of wider space on terminals.
* Supports colored terminal strings (Only for Linux currently) and full-width characters.

Still, **[pptree](https://github.com/clemtoy/pptree) is a wonderful package**. The implementation is really beautiful and I borrowed some ideas from the author.

### Documentation
The `print*.py` files in the `example` directory provides several examples on how to use the package. And below can be regard as an explanation of these files. The files in `example` directory enables coloring to demonstrate the ability of this package to print tree with colors. Because the effect can not be seen in this md file, corresponding codes are ommited.
Suppose we have the `Node` class:
```python
class Node(object):

    def __init__(self, value, parent):
        self.value = value
        self.children = []
        if parent is not None:
            parent.children.append(self)
```
As an example, let's construct a tree as follows:
```python
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
```
To print the tree, we have to tell `print_tree` two things:
1. how to transverse the tree from the root node.
2. how to interpret every node as a string. 

To achieve these goals, we inherent `print_tree` from the package then override `get_children` and `get_node_str`:
```python
from print_tree import print_tree

class print_custom_tree(print_tree):

    def get_children(self, node):
        return node.children

    def get_node_str(self, node):
        return str(node.value)
```
`get_children` should accept a `Node` and return a list with element type `Node` or `PlaceHolder` (see below for more info on `PlaceHolder`), and `get_node_str` accept a `Node` and return a string. Then we can use `print_custom_tree` as if it's a function:
```
>>> print_custom_tree(data_structure)

             ┌Vector
             ├List
Data Stucture┤
             │    ┌AVL
             │    ├Splay
             ├Tree┼B
             │    ├Quand
             │    └kd
             └Graph─DAG
```
Below is a colored version if you run the file in the `example` directory:

![](https://user-images.githubusercontent.com/22628546/47987611-eb6d2c80-e11a-11e8-96bd-35b2370a8c5d.gif)

If you feel uncomfortable about the naming of the class, you can import `PrintTree` then use `PrintTree` instead. 

Now let's move on to some more complex examples. In the `example` directory I have defined a primitive search tree with custom numbers of branch. For brevity only the `__init__` function of the `Node` is shown here. If `branch == 2` then it's a binary search tree.
```python
class Node(object):

    def __init__(self, value, branch):
        self.values = [value]
        self.branch = branch
        self.children = [None] * branch
```
If we wish to emphasize on the *binary* structure, we can override `get_children` and `get_node_str` as follows:
```python
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
        return str(node.values[0])
```
In this case it is possible that the return list of `get_children` contains `PlaceHolder`, which can be directly imported by `from print_tree import PlaceHolder`. If `PlaceHolder` is in the return list, `print_tree` will take it as a placeholder: nothing will be shown, but it takes blank space:
```
# Tree (bst) already initialized
>>> print_binary(bst.root)

        ┌19┐
        │  │  ┌18
        │  └17┤
        │     │  ┌16
        │     └15┘
        │       
        │       
     ┌14┤
     │  └13
  ┌12┘
  │ 
  │ 
11┤
  │     ┌10
  │   ┌9┤
  │   │ └8
  │ ┌7┤
  │ │ │   ┌6
  │ │ │ ┌5┤
  │ │ │ │ │ ┌4
  │ │ │ │ └3┘
  │ │ │ │   
  │ │ └2┤
  │ │   └1
  └0┘
```
Because the tree is randomly generated, the result is probably different from what you saw when you test your installation. However, in both cases, you can read the inorder transverse of the tree from bottom to top as `list(range(20))` (0 to 19).

The effect of `PlaceHolder` becomes prominent after we delete them (also note on the benefit of inheritance):
```python
class print_binary_without_placeholder(print_binary):
    def get_children(self, node):
        l_child, r_child = node.children
        children = []
        if r_child is not None:
            children.append(r_child)
        if l_child is not None:
            children.append(l_child)
        return children

# initialize the tree(bst)
...

print_binary_without_placeholder(bst.root)

              ┌18
        ┌19─17┤
        │     └15─16
  ┌12─14┤
  │     └13
11┤
  │     ┌10
  │   ┌9┤
  │   │ └8
  └0─7┤
      │   ┌6
      │ ┌5┤
      │ │ └3─4
      └2┤
        └1
```
