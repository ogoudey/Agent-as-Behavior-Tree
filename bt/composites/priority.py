#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 4.0.0 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt_library as btl

from typing import List

class Priority(btl.Composite):
    """
    Specific implementation of the priority composite.
    """

    def __init__(self, name: str, priorities: List[int], children: btl.NodeListType):
        """
        Default constructor.

        :param name: Name of the node
        :param children: List of children for this node
        :param priorities: Corresponding priorities for each child
        """
        super().__init__(name, children)
        self.priorities = priorities

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """
        running_child = self.additional_information(blackboard, 0)
        """
        print(len(self.children))
        print(len(self.priorities))
        for i in self.priorities:
            print(i)
        """
        sorted_children = [self.children[i] for i in self.priorities] # reorders according to priority parameter
        
        for child_position in range(running_child, len(sorted_children)):
            child = sorted_children[child_position]

            result_child = child.run(blackboard)
            if result_child == btl.ResultEnum.SUCCEEDED:
                return self.report_succeeded(blackboard, 0)

            if result_child == btl.ResultEnum.RUNNING:
                return self.report_running(blackboard, child_position)

        return self.report_failed(blackboard, 0)
