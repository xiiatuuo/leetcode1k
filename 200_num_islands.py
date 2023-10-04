#
# @lc app=leetcode.cn id=200 lang=python
#
# [200] 岛屿数量
#

# @lc code=start
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        isLands  = 0
        def dfs(grid, i, j):
            # print("i=%s|j=%s" %(i,j))
            if i >= len(grid) or i<0 or j >= len(grid[i]) or j<0:
                return 0
            if grid[i][j] == '0':
                return 0
            grid[i][j] = '0'
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)
            
            return 1
            
        for i in xrange(len(grid)):
            for j in xrange(len(grid[i])):
                if grid[i][j] == '0':
                    continue
                # print("dfs input:i=%s|j=%s" %(i,j))
                isLands += dfs(grid, i, j)
        return isLands

