#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 20200130 v1
#
# 1- 改进, 利用if l1 代替 if l1 == None, 使得表达更加简练
# 2- 最后返回的是dummy_head.next, 浪费一个节点, 使得表达更加的简练(跟commit 1045198 比较额)
#
# 1563/1563 cases passed (64 ms)
# Your runtime beats 95.01 % of python3 submissions
# Your memory usage beats 59.21 % of python3 submissions (13.2 MB)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0;
        dummy_head = ListNode(0)
        current = dummy_head

        while l1 or l2 or carry == 1:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = sum // 10
            sum = sum % 10

            current.next = ListNode(sum)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy_head.next
# @lc code=end
