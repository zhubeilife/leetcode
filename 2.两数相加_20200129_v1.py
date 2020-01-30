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

# 20200119 v1
# 采用把连个数字给拆出来的方法来做, 通过看leetcode讨论, 在C++中会出现long long这种数据类型都会溢出的情况, 然后看到python(In Python, value of an integer is not restricted by the number of bits and can expand to the limit of the available memory) 原因所以不会溢出.
#
# 1- 所以应该尝试采用链表直接相加的方式
# 2- 另外链表转化的时候, 其实可以采用string, 而不用List
#
# 1563/1563 cases passed (84 ms)
# Your runtime beats 39.44 % of python3 submissions
# Your memory usage beats 59.61 % of python3 submissions (13.2 MB)

class Solution:
    def parse_num(self, input_list: ListNode) -> int:
        # parse the digital nums
        dig_items = []
        while input_list.next != None:
            dig_items.append(input_list.val)
            input_list = input_list.next
        dig_items.append(input_list.val)

        # get the real nums
        real_num = 0
        for i, n in enumerate(dig_items):
            real_num += n * pow(10, i)

        return real_num

    def code_num(self, real_number):
        dig_items = []
        dig_items.append(real_number % 10)
        real_number = real_number // 10
        while real_number != 0:
            dig_items.append(real_number % 10)
            real_number = real_number // 10

        result = ListNode(dig_items[0])
        result.next = None
        current = result

        for i in range(len(dig_items) - 1):
            new_item = ListNode(dig_items[i + 1])
            new_item.next = None
            current.next = new_item
            current = new_item

        return result

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = self.parse_num(l1) + self.parse_num(l2)
        return self.code_num(sum)

# @lc code=end
