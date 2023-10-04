#
# @lc app=leetcode.cn id=198 lang=python
#
# [198] 打家劫舍
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1 :
            return nums[0]
        dp = []
        dp = [ [0,0] for _ in xrange(len(nums))]
        dp[0][0] = 0
        dp[0][1] = nums[0]
        ans = 0
        for i in xrange(1, len(nums)):
            dp[i][0] = dp[i-1][1]
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+nums[i])
            if dp[i][0] > ans:
                ans = dp[i][0]
            if dp[i][1] > ans:
                ans = dp[i][1]
        return ans
        
