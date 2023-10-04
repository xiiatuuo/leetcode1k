#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        left_set = set(['(', '{','['])
        right_set = set(['}', ')',']'])
        pair_dict = {'(':')','[':']','{':'}'}
        if len(s) % 2 != 0 :
            return False
        for i in xrange(len(s)):
            if s[i] in left_set:
                stack.append(s[i])
            elif s[i] in right_set:
                if not len(stack):
                    return False
                t = stack.pop()
                if s[i] != pair_dict[t]:
                    return False
        if len(stack):
            return False
        return True
