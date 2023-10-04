#
# @lc app=leetcode.cn id=88 lang=python
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        i, j, p = m-1, n-1, m+n-1
        while i >=0 and j >=0:
            print("i=%s|j=%s|p=%s" %(i,j,p))
            if nums1[i] <= nums2[j]:
                nums1[p] = nums2[j]
                p = p - 1
                j = j - 1
            else:
                nums1[p] = nums1[i]
                p = p - 1
                i = i - 1
        while j >= 0:
            nums1[p] = nums2[j]
            p = p - 1 
            j = j - 1

