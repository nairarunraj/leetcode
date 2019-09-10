#!/usr/bin/env python3

# Problem Statement - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def display(self):
        result_list = []
        current_node = self
        while current_node:
            result_list.append(current_node.val)
            current_node = current_node.next

        print(result_list)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(-1)
        self.addTwoLLNumbers(l1, l2, result, 0)
        return result
    
        
    def addTwoLLNumbers(self, l1: ListNode, l2: ListNode, res: ListNode, carry: int) -> None:
        if l1 and l2:
            #print("%d - %d - %d" % (l1.val, l2.val, carry))
            sum = carry + l1.val + l2.val
        elif l1:
            #print("%d - x - %d" % (l1.val, carry))
            sum = carry + l1.val
        elif l2:
            #print("x - %d - %d" % (l2.val, carry))
            sum = carry + l2.val
        elif not carry:
            #print("x - x - %d" % (carry))
            return
        else:
            #print("x - x - %d" % (carry))
            sum = carry
            
        unit_digit = sum % 10
        carry_forward = int(sum/10)

        if res.val == -1:
            res.val = unit_digit
            self.addTwoLLNumbers(l1.next, l2.next, res, carry_forward)
        else:
            result = ListNode(unit_digit)
            res.next = result
            
            l1_next = None
            if l1:
                l1_next = l1.next
            
            l2_next = None
            if l2:
                l2_next = l2.next
            
            self.addTwoLLNumbers(l1_next, l2_next, result, carry_forward)


if __name__ == "__main__":
    solution = Solution()
    list_1 = [5,6,7]
    list_2 = [9,9,9,9]

    prev = None
    l1 = None
    for num in list_1:
        node = ListNode(num)
        if prev:
            prev.next = node
        else:
            l1 = node
        prev = node

    prev = None
    l2 = None
    for num in list_2:
        node = ListNode(num)
        if prev:
            prev.next = node
        else:
            l2 = node
        prev = node

    l1.display()
    l2.display()
    result = solution.addTwoNumbers(l1, l2)

    result.display()
