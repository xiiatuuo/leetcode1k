#
# @lc app=leetcode.cn id=93 lang=python
#
# [93] 复原 IP 地址
#

# @lc code=start
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or len(s)<=3:
            return []

        result_list  = []
        path = []

        def is_valid_str(s, st, et):
            length = et - st
            if  length <= 0 or length>3:
                return False
            if s[st]=='0' and length>1:
                return False 
            try:
                s_int = int(s[st:et])
            except Exception(e):
                s_int = -1
            if s_int >=0 and s_int<=255:
                return True
            else:
                return False

        def backstrace(s, path, st):
            if len(path) == 4 and st == len(s):
                result_list.append('.'.join(path))
                return
            if len(path) > 4 or st > len(s):
                return 
            for i in xrange(3):
                et = st + i + 1
                if et > len(s):
                    break
                if is_valid_str(s,st, et):
                    path.append(s[st:et])
                    backstrace(s, path, et)
                    path.pop()
                
        backstrace(s,path, 0)
        return result_list 


