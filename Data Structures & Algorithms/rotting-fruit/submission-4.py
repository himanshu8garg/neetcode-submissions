class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue=deque()
        visit = set() ## we dont need since we mark a fruit rotten so we dont ever see it again 
        fresh, time = 0,0

        #LETS GET ALL THE ROTTEN ORANGES AND FRESH COUNT

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh +=1
                if grid[i][j] == 2:
                    queue.append((i,j))
        
        ## NOW WE HAVE OUR QUEUE:
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        while queue and fresh >0:
        
            for i in range(len(queue)):
                r,c = queue.popleft()
                ## CHECK ALL 4 directions
                for dr, dc in directions:
                    row = r+dr
                    col = c+dc
                    if (row < len(grid) and col < len(grid[0]) and col >= 0 and row >= 0 and grid[row][col] == 1):
                        grid[row][col] = 2
                        queue.append((row, col))
                        fresh -=1

            time+=1
        return time if fresh == 0 else -1
                