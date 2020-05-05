# -*- coding: UTF-8 -*-

__author__ = 'Shezzer'


# 2. 两数相加
# medium
# 链表 数学

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Solution
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        node = head
        flag = False
        while l1 or l2:
            newNode = ListNode(0)
            node.next = newNode
            node = newNode
            sum = 0
            if flag:
                sum += 1
                flag = False
            if l1 and l2:
                sum += l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1:
                sum += l1.val
                l1 = l1.next
            else:
                sum += l2.val
                l2 = l2.next

            if sum >= 10:
                sum -= 10
                flag = True
            node.val = sum

        if flag:
            node.next = ListNode(1)

        return head.next


def traverse(ln: ListNode):
    while ln:
        if ln.next is not None:
            print('%d -> ' % ln.val, end='')
        else:
            print(ln.val)
        ln = ln.next


if __name__ == '__main__':
    ls = [4, 3]
    node1 = ListNode(2)
    node = node1
    for i in ls:
        node.next = ListNode(i)
        node = node.next

    ls = [6, 4]
    node2 = ListNode(5)
    node = node2
    for i in ls:
        node.next = ListNode(i)
        node = node.next

    res = Solution().addTwoNumbers(node1, node2)

    traverse(res)
