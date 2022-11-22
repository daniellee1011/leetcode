"""
Test Cases: 61/77
Wrong solution.
Bipartite algorithm can be a solution algorithm for this problem.
It is possible to make this code to get all expected output,
but caught by Time Limit Exceeded in this way.
"""

class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        c = 0
        cM = 0
        col = [0] * m

        for i in range(m):
            for j in range(n):
                col[i] += grid[i][j]
            if cM < col[i]:
                cM = col[i]
            if col[i] != 0:
                c += 1
            grid[i].append(col[i])
       
        grid.sort(key = lambda x:x[n])

        visited = [0] * n

        def dfs(rI, cI, cnt):
            flag = 0
            if(rI == m):
                return cnt
            for i in range(rI, m):
                for j in range(n):
                    if grid[i][j] == 1 and visited[j] == 0:
                        visited[j] = 1
                        return dfs(i+1, i, cnt+1)
                        visited[j] = 0
                        flag = 1
                if flag == 1:
                    break
                if i == m-1:
                    return cnt

        ret = 0
        flag = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    visited[j] = 1
                    tmp = dfs(i+1, j, 1)
                    visited[j] = 0
                    if tmp != None and tmp > ret:
                        ret = tmp
                    flag = 1
        
        return ret
