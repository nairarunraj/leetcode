# Definition for a binary tree node.

import copy

import pytest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return f"(Val: {self.val}, left: {self.left}, right: {self.right})"


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(orig_node: TreeNode, cloned_node: TreeNode, target: TreeNode) -> TreeNode:
            if orig_node is None:
                return None

            if orig_node is target:
                return cloned_node

            if left_search := dfs(orig_node.left, cloned_node.left, target):
                return left_search

            return dfs(orig_node.right, cloned_node.right, target)

        return dfs(original, cloned, target)


@pytest.fixture
def solution():
    return Solution()


def build_rest_nodes(tree, current_node, current_index):
    if current_node is None:
        return

    left_child = current_index * 2 + 1
    right_child = current_index * 2 + 2

    right_node = left_node = None

    if left_child < len(tree) and tree[left_child] != 'null':
        left_node = TreeNode(tree[left_child])

    if right_child < len(tree) and tree[right_child] != 'null':
        right_node = TreeNode(tree[right_child])

    current_node.left = left_node
    current_node.right = right_node

    build_rest_nodes(tree, current_node.left, left_child)
    build_rest_nodes(tree, current_node.right, right_child)


def build_tree(tree):
    head_node = TreeNode(tree[0])

    build_rest_nodes(tree, head_node, 0)

    return head_node


def get_target_node(orig_node, target):
    if orig_node is None or orig_node.val == target:
        return orig_node

    if left_search := get_target_node(orig_node.left, target):
        return left_search

    return get_target_node(orig_node.right, target)


def generate_inputs(tree, target):
    original = build_tree(tree)
    cloned = copy.deepcopy(original)
    target_node = get_target_node(original, target)

    return original, cloned, target_node


def test_solution1(solution):
    tree = [7, 4, 3, 'null', 'null', 6, 19]
    target = 3

    (original, cloned, target_node) = generate_inputs(tree, target)

    assert target_node.val == solution.getTargetCopy(original, cloned, target_node).val


def test_solution2(solution):
    tree = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 5

    (original, cloned, target_node) = generate_inputs(tree, target)

    assert target_node.val == solution.getTargetCopy(original, cloned, target_node).val


def test_solution3(solution):
    tree = [1, 2, 'null', 3]
    target = 2

    (original, cloned, target_node) = generate_inputs(tree, target)

    assert target_node.val == solution.getTargetCopy(original, cloned, target_node).val


if __name__ == '__main__':
    solution = Solution()
    test_solution1(solution)
