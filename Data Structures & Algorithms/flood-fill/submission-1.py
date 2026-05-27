class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        og_color = image[sr][sc]
        if image[sr][sc] == color:
                return image
        def dfs(r,c):
            # CHECK FOR OOB 
            if r<0 or r>=rows or c<0 or c>=cols or image[r][c]!=og_color:
                return
            ##If we are here it means we need to switch teh color and check all four directions
            image[r][c]=color
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
    
        dfs(sr,sc)
        return image

           
            
