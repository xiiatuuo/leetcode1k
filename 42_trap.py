#
# @lc app=leetcode.cn id=42 lang=python
#
# [42] 接雨水
#

# @lc code=start
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2:
            return 0


        left_max = [0 for i in height]
        right_max = [0 for i in height]
        left_max[0] = height[0]
        right_max[len(height)-1] = height[len(height)-1]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i-1], height[i])
        for i in range(len(height)-2,0,-1):
            right_max[i] = max(right_max[i+1], height[i])


        ans = 0
        for i in xrange(len(height)):
            if i == 0 or i == len(height)-1:
                continue
            h = min(left_max[i],right_max[i]) - height[i]
            if h > 0:
                ans = ans + h
        return ans
