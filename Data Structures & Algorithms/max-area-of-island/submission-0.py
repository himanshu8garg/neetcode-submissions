class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r,c):
            if r == rows or c ==cols or r<0 or c<0 or grid[r][c] == 0 or (r,c) in visited:
                return 0
            
            visited.add((r,c))
            return(1 + 
                    dfs(r+1,c) +
                    dfs(r,c+1) +
                    dfs(r-1,c) +
                    dfs(r,c-1))


        area = 0
        for i in range(rows):
            for j in range(cols):
                area= max(area, dfs(i,j))
        
        return area 
