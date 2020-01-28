#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# 2020-01-08 v2
#
# 这个版本是根据网上介绍的用hash来实现查找, 因为hash为O(1)
#
# Result
# 29/29 cases passed (56 ms)
# Your runtime beats 86.37 % of python3 submissions
# Your memory usage beats 69.29 % of python3 submissions (14.3 MB)

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i,num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i!=j:
                return [i,j]

            hashmap[num] = i
        # return result
# @lc code=end
