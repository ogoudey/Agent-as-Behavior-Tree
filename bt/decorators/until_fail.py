from bt_library.blackboard import Blackboard
from bt_library.common import ResultEnum
from bt_library.decorator import Decorator
from bt_library.tree_node import TreeNode


class UntilFail(Decorator):
    """
    Specific implementation of the timer decorator.
    """

    def __init__(self, child: TreeNode):
        """
        Default constructor.

        :param name: Name of the node
        :param time: Duration of the timer [counts]
        :param child: Child associated to the decorator
        """
        super().__init__('Until Fail', child)

    def run(self, blackboard: Blackboard) -> ResultEnum:
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """
        # Evaluate the child
        result_child = self.child.run(blackboard)


        # If the child failed, terminate immediately the timer
        return self.report_succeeded(blackboard) \
            if result_child == ResultEnum.FAILED \
            else self.report_running(blackboard)
