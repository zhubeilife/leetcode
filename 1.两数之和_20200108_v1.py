#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# 2020-01-08 v1
#
# 这个版本主要的想法就是遍历真个List找到对应的a+b=target, 找到对应的b.
#
# 1- 首先是先sort, 这样的话就不用搜索整个的空间, 只用搜索 target/2 就可以
# 2- 遇到的问题就是, 程序需要返回的是原List的下标; 如果是两个相同的书相加
# 3- 费时间的部分应该是查找, sort虽然也能让查找更快一些, 但是还是比较费时间
#
# Result
# 29/29 cases passed (56 ms)
# Your runtime beats 86.37 % of python3 submissions
# Your memory usage beats 76.34 % of python3 submissions (14.2 MB)
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sort_nums = sorted(nums)
        target_middle = target / 2
        result = []
        for i, a in enumerate(sort_nums):
            if (target - a) in sort_nums[(i+1):]:
                result.append(nums.index(a))
                # TODO
                # Here is the hack to avoid the same value
                if (target - a) == a:
                    result.append(nums.index(target -a, result[0]+1))
                else:
                    result.append(nums.index(target -a))
                break
        return result
# @lc code=end

