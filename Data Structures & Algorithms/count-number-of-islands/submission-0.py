class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ## WE ALSO NEED TO KEEP TRACK IF WE HAVE VISITED THE ISLAND BEFORE 
        islands = 0
        visited = (0,0)
        def dfs(r,c):
            ## CHECK FOR OOB
            if r == len(grid) or c == len(grid[0]) or r<0 or c<0 or grid[r][c] == "0":
                return

            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r+dr,c+dc)

        for r in range(row):
            for c in range(cols):
                if grid[r][c] =="1":
                    dfs(r,c)
                    islands+=1

        return islands
        