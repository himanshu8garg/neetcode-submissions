class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ## LETS BUILD AN ADJACENY LIST
        adj_map = {}
        for i in range(numCourses):
            adj_map[i] = []
        for crs, pre in prerequisites:
            adj_map[crs].append(pre)
            
        print (adj_map)
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if (adj_map[crs] == []):
                return True
            
            visited.add(crs)
            for pre in adj_map[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            adj_map[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True         

   
