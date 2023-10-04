#
# @lc app=leetcode.cn id=51 lang=python
#
# [51] N 皇后
#

# @lc code=start
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        col_set,row_set,pie_set,na_set = set([]),set([]),set([]),set([])
        index_result,result_list = [],[]

        def do(n, row, index_info):
            if row >= n:
                index_result.append(index_info)
                return
            for i in xrange(n):
                if i in col_set or row+i in pie_set or row-i in na_set:
                    continue
                col_set.add(i)
                pie_set.add(row+i)
                na_set.add(row-i)
                # index_info.append(i)
                new_index_info = [_ for _ in index_info]
                new_index_info.append(i)
                do(n, row+1, new_index_info)
                col_set.remove(i)
                pie_set.remove(row+i)
                na_set.remove(row-i)
                # index_info = index_info[:-1]

        
        def construct(index_result,result_list,n):
            for index_info in index_result:
                solution_list = []
                for i in range(len(index_info)):
                    res_list = [ "." for _ in range(n)]
                    index = index_info[i]
                    res_list[index] = 'Q'
                    solution_list.append("".join(res_list))
                result_list.append(solution_list)

        do(n, 0, [])
        print(index_result)
        construct(index_result,result_list,n)
        return result_list
