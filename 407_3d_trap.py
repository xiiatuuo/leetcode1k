#
# @lc app=leetcode.cn id=407 lang=python
#
# [407] 接雨水 II
#

# @lc code=start
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if len(heightMap) < 3:
            return 0 
        if len(heightMap[0]) < 3:
            return 0
        r = len(heightMap)
        c = len(heightMap[0])
        visited = [[0 for _ in heightMap[0]] for _ in heightMap]
        pq = []
        for i in xrange(r):
            for j in xrange(c):
                if i==0 or i==r-1 or j==0 or j==c-1:
                    visited[i][j] = 1
                    heapq.heappush(pq, (heightMap[i][j], i, j))
        ans = 0 
        dirs = [-1, 0, 1, 0, -1]
        while len(pq):
            h, x, y = heapq.heappop(pq)
            for k in range(4):
                nx = x + dirs[k]
                ny = y + dirs[k+1]
                if nx >=0 and nx < r and ny>=0 and ny<c and not visited[nx][ny]:
                    if h > heightMap[nx][ny]:
                        ans = ans + h - heightMap[nx][ny]
                    visited[nx][ny] = 1
                    heapq.heappush(pq, (max(h,heightMap[nx][ny]), nx, ny))
        return ans
