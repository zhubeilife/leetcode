#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def decode_num(self, L):
        num_list = []

        while True:
            num_list.append(L.val)
            if L.next is None:
                break
            else:
                L = L.next

        real_num = 0
        for i in range(len(num_list)):
            real_num += num_list[i] * (10 ** i)

        return real_num


    def code_num(self, num):
        digit_counts = len(str(num))

        for i in range(digit_counts):


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # parse the real nums out of Listnode
        num_one = self.parse_num(l1)
        num_two = self.parse_num(l2)

        sum = num_one + num_two

