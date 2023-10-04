#
# @lc app=leetcode.cn id=22 lang=python
#
# [22] 括号生成
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def do(res, s, left, right, n):
            if left > n or right > n or right > left:
                return 
            if left == n and right == n:
                res.append(s)
                return
            
            do(res, s+")", left, right+1, n)
            do(res, s+"(", left+1, right, n)
           
        res = []
        do(res, "", 0, 0, n)
        return res

