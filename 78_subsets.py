#
# @lc app=leetcode.cn id=78 lang=python
#
# [78] 子集
#

# @lc code=start
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def recursion(cur, n, r, result):
            if cur == n:
                result.append(r)
                return
            #s1 = [i for i in r]
            #recursion(cur+1, n, s1, result)
            #s2 = [i for i in r]
            #s2.append(nums[cur])
            #recursion(cur+1, n, s2, result)  
            recursion(cur+1, n, r, result)
            recursion(cur+1, n, r+[nums[cur]], result)  
              
        result = []
        recursion(0, len(nums), [], result) 
        return result

