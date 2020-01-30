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

# 20200119 v2
# 采用把连个数字给拆出来的方法来做, 通过看leetcode讨论, 在C++中会出现long long这种数据类型都会溢出的情况, 然后看到python(In Python, value of an integer is not restricted by the number of bits and can expand to the limit of the available memory) 原因所以不会溢出.
#
# 在v1的基础上, 采用string来进行数字的转换
#
# 1563/1563 cases passed (80 ms)
# Your runtime beats 51.35 % of python3 submissions
# Your memory usage beats 59.62 % of python3 submissions (13.1 MB)

class Solution:
    def parse_num(self, input_list: ListNode) -> int:
        # parse the digital nums
        dig_items = ''
        while input_list != None:
            dig_items = str(input_list.val) + dig_items
            input_list = input_list.next

        return int(dig_items)

    def code_num(self, real_number):
        dig_items = str(real_number)

        result = ListNode(dig_items[-1])
        current = result

        for i in range(len(dig_items) - 1, 0, -1):
            current.next = ListNode(dig_items[i - 1])
            current = current.next

        return result

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = self.parse_num(l1) + self.parse_num(l2)
        return self.code_num(sum)

# @lc code=end
