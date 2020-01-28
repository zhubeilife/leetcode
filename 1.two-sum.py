#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # sort list first
        nums_dict = {i : nums[i] for i in range(0, len(nums))}

        sort_dict = sorted(nums_dict.items(), key=lambda x: x[1])

        x = 0
        y = len(nums) - 1

        while x != y:
            sum = sort_dict[x][1] + sort_dict[y][1]
            if  sum == target:
                return [sort_dict[x][0], sort_dict[y][0]]
            elif sum < target:
                x += 1
            else:
                y -= 1

        return None

