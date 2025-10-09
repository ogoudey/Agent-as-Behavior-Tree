#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# version 4.0.0 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt as bt
import bt_library as btl
# Instantiate the tree according to the assignment. The following are just examples.

# Example 1:
# tree_root = bt.Timer('timer_1', 5, bt.FindHome())

# Example 2:
# tree_root = bt.Selection(
#     'selection_1',
#     [
#         BatteryLessThan30(),
#         FindHome()
#     ]
# )

tree_root = bt.Sequence("Main Sequence",
    [
        bt.SetGetNameInstructions(),
        bt.GetName(),
        bt.Done()
    ]
)

robot_behavior = btl.BehaviorTree(tree_root)
