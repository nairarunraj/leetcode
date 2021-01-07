# Definition for singly-linked list.
from typing import List, Tuple

import pytest


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

    def __str__(self):
        return f"{self.val}, {self.next}"


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        if head.val == head.next.val:
            # skip duplicate nodes
            while head.next and head.val == head.next.val:
                head = head.next
            return self.deleteDuplicates(head.next)
        else:
            head.next = self.deleteDuplicates(head.next)
            return head

    def _deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        next_node = head.next

        if head.val == next_node.val:
            while next_node and head.val == next_node.val:
                next_node = next_node.next

            head = self.deleteDuplicates(next_node)

        def delete_rest(curr: ListNode) -> None:
            if not curr:
                return

            prev = curr
            current_node = curr.next
            if not current_node:
                return

            next_node = current_node.next

            if next_node and current_node.val == next_node.val:
                while next_node and current_node.val == next_node.val:
                    next_node = next_node.next

                prev.next = next_node
                delete_rest(prev)
            else:
                delete_rest(current_node)

        delete_rest(head)

        return head


@pytest.fixture
def solution():
    return Solution()


def get_linked_list(arr: List) -> ListNode:
    prev = None
    head = None
    for val in arr:
        node = ListNode(val)
        if not head:
            head = node
            prev = head
        else:
            prev.next = node
            prev = node

    return head


def get_arr(head: ListNode) -> Tuple:
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next

    return tuple(arr)


def test_solution1(solution):
    arr = [1, 2, 3, 3, 4, 4, 5]
    head = get_linked_list(arr)
    dedup_arr = (1, 2, 5)
    dedup_ll = solution.deleteDuplicates(head)

    assert dedup_arr == get_arr(dedup_ll)


def test_solution2(solution):
    arr = [1]
    head = get_linked_list(arr)
    dedup_arr = (1,)
    dedup_ll = solution.deleteDuplicates(head)

    assert dedup_arr == get_arr(dedup_ll)


def test_solution3(solution):
    arr = [1, 1, 2, 2]
    head = get_linked_list(arr)
    dedup_arr = ()
    dedup_ll = solution.deleteDuplicates(head)

    assert dedup_arr == get_arr(dedup_ll)
