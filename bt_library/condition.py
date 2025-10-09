#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 4.0.0 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

from .tree_node import TreeNode


class Condition(TreeNode):
    """
    The generic definition of the condition node class.
    """

    def __init__(self, name: str):
        """
        Default constructor.

        :param name: Name of the node
        """
        super().__init__(name)
