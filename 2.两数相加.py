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
# 采用把连个数字给拆出来的方法来做, 通过看leetcode讨论, 在C++中会出现long long这种数据类型都会溢出的情况, 然后看到python(In Python, value of an integer is not restricted by the number of bits and can expand to the limit of the available memory) 原因所以不会溢出.
#
# 在v1的基础上, 采用string来进行数字的转换
#
# 1563/1563 cases passed (80 ms)
# Your runtime beats 51.35 % of python3 submissions
# Your memory usage beats 59.62 % of python3 submissions (13.1 MB)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0;
        result = ListNode(0)
        current = result

        while True:
            sum = (l1.val if l1 != None else 0) + (l2.val if l2 != None else 0) + carry
            carry = sum // 10
            sum = sum % 10

            current.val = sum

            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None

            if l1 == None and l2 == None and carry == 0:
                break

            current.next = ListNode(0)
            current = current.next

        return result
# @lc code=end
