#
# @lc app=leetcode.cn id=46 lang=python
#
# [46] 全排列
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result_list = []
        used = set([])

        def recursion(d, n, used, info):
            if d == n:
                result_list.append(info)
            for i in xrange(n):
                if nums[i] in used:
                    continue
                used.add(nums[i])
                recursion(d+1, n, used, info+[nums[i]])
                used.remove(nums[i])            

        recursion(0, len(nums), used, [])
        return result_list
