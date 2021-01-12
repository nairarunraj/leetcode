import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if self.next:
            return f"{self.val},{self.next}"
        return f"{self.val}"


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        prev = None
        sum_head_node = None
        while l1 and l2:
            sum_ = l1.val + l2.val + carry
            (carry, val) = divmod(sum_, 10)
            digit_node = ListNode(val)
            if prev:
                prev.next = digit_node
            else:
                sum_head_node = digit_node

            prev = digit_node
            l1 = l1.next
            l2 = l2.next

        while l1:
            sum_ = l1.val + carry
            (carry, val) = divmod(sum_, 10)
            digit_node = ListNode(val)
            if prev:
                prev.next = digit_node
            else:
                sum_head_node = digit_node

            prev = digit_node

            l1 = l1.next

        while l2:
            sum_ = l2.val + carry
            (carry, val) = divmod(sum_, 10)
            digit_node = ListNode(val)
            if prev:
                prev.next = digit_node
            else:
                sum_head_node = digit_node

            prev = digit_node
            l2 = l2.next

        if carry:
            carry_node = ListNode(1)
            prev.next = carry_node

        return sum_head_node


@pytest.fixture()
def solution():
    return Solution()


def build_ll(number_list):
    prev = None
    head = None
    for no in number_list:
        digit_node = ListNode(no)
        if prev:
            prev.next = digit_node
        else:
            head = digit_node

        prev = digit_node

    return head


def get_sum_list(sum_ll):
    sum_list = []
    while sum_ll:
        sum_list.append(sum_ll.val)
        sum_ll = sum_ll.next

    return sum_list


def test_solution1(solution):
    no1 = [2, 4, 3]
    no2 = [5, 6, 4]

    l1 = build_ll(no1)
    l2 = build_ll(no2)

    sum_ll = solution.addTwoNumbers(l1, l2)

    assert "7,0,8" == str(sum_ll)


def test_solution2(solution):
    no1 = [0]
    no2 = [0]

    l1 = build_ll(no1)
    l2 = build_ll(no2)

    sum_ll = solution.addTwoNumbers(l1, l2)

    assert "0" == str(sum_ll)


def test_solution3(solution):
    no1 = [9, 9, 9, 9, 9, 9, 9]
    no2 = [9, 9, 9, 9]

    l1 = build_ll(no1)
    l2 = build_ll(no2)

    sum_ll = solution.addTwoNumbers(l1, l2)

    assert "8,9,9,9,0,0,0,1" == str(sum_ll)
