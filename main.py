#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# version 4.0.0 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt_library as btl
import time
from bt.behavior import robot_behavior
from collections import defaultdict

def main():
# Main body of the assignment
    current_blackboard = btl.Blackboard()

    # You must determine what to store in the blackboard. This is just an example.

    # You must determine how your solution terminates. This is just an example.
    done = 1000


    current_blackboard.set_in_environment('DONE', False)

    while not current_blackboard.get_in_environment('DONE', False):
            btl.print_blackboard('BLACKBOARD BEFORE', current_blackboard)
            btl.print_header('TREE EVALUATION')
            result = robot_behavior.evaluate(current_blackboard)
            btl.print_footer()
            # Print the state of the tree nodes before the evaluation
            btl.print_blackboard('BLACKBOARD AFTER', current_blackboard)
            
if __name__ == "__main__":
    main()



