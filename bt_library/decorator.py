#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 4.0.0 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

from .tree_node import TreeNode


class Decorator(TreeNode):
    """
    The generic definition of the decorator node class.
    """
    __child: TreeNode  # Child associated with this decorator

    def __init__(self, name: str, child: TreeNode):
        """
        Default constructor.

        :param name: Name of the node
        :param child: Child for this node
        """
        super().__init__(name)

        self.__child = child

    @property
    def child(self) -> TreeNode:
        """
        :return: Return the child associated with this decorator
        """
        return self.__child
