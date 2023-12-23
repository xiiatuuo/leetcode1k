#
# @lc app=leetcode.cn id=31 lang=python
#
# [31] 下一个排列
#

# @lc code=start
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        pos = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] >= nums[i+1]:
                continue
            else:
                ans = nums[i+1] - nums[i]
                pos = i
                break
        if pos < 0:
            return nums.reverse()
        
        for j in xrange(len(nums)-1, -1,-1):
            if nums[j] > nums[pos]:
                nums[j], nums[pos] = nums[pos],nums[j]
                break
        left , right = pos + 1, len(nums)-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums
