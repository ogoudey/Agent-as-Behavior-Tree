#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 4.0.0 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#
from . import STATE_NODE
from .blackboard import Blackboard
from .common import STATE_NODE_RESULT, STATE_ADDITIONAL_INFORMATION, ResultEnum, NodeIdType


def cancel_running(blackboard: Blackboard):
    """
    Cancel the running state of every node in the blackboard.

    :param blackboard: Blackboard with the current state to query
    """
    # First, find all the tree nodes in a RUNNING state. The blackboard cannot be modified
    # during the traversal
    running_nodes = []
    for node in blackboard.states():
        tree_node_id = NodeIdType(node[0])
        result = ResultEnum(node[1][STATE_NODE_RESULT])

        if result == ResultEnum.RUNNING:
            running_nodes.append(tree_node_id)

    # Remove all  nodes
    for running_node_id in running_nodes:
        blackboard.remove_state(running_node_id)

def print_blackboard(title: str, blackboard: Blackboard):
    """
    Print the state of every node in the blackboard.

    :param title: Title of the print
    :param blackboard: Blackboard to print
    """
    print_header(title)
    print_environment(blackboard)
    print()
    print_states(blackboard)
    print_footer()

def print_environment(blackboard: Blackboard):
    """
    Print the environment variables in the blackboard..

    :param blackboard: Blackboard to print
    """
    for variables in blackboard.environment():
        key = variables[0]
        value = variables[1]

        if isinstance(value, str):
            print(f'{key} = "{value}"')
        else:
            print(f'{key} = {value}')

def print_footer():
    """
    Print a footer message.
    """
    print('=' * 120)
    print()

def print_header(title: str):
    """
    Print a header message.

    :param title: Title of the header
    """
    print('=' * 120)
    print(title)
    print('-' * 120)

def print_states(blackboard: Blackboard):
    """
    Print the state of every node in the blackboard.

    :param blackboard: Blackboard to print
    """
    for single_state in blackboard.states():
        state = single_state[1]

        print(f'Node: {state[STATE_NODE].pretty_id}, '
              f'Result: {ResultEnum(state[STATE_NODE_RESULT])}, '
              f'Additional information: {state[STATE_ADDITIONAL_INFORMATION]}')
