class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(i, comb):
            if i > n:
                if len(comb) == k:
                    res.append(comb.copy())
                return

            comb.append(i)
            backtrack(i+1, comb)
            comb.pop()
            backtrack(i+1,comb)
        
        backtrack(1,[])
        return res



        # currSet, result = [],[]
  
        # ## AT EACH NODE WE CAN EITHER INCLUDE OR NOT INCLUDE A NUMBER, but we only wanna go the values grater than what we are at 
        # def dfs(start, comb):

        #     if len(comb)==k:
        #         result.append(comb.copy())
        #         return

        #     for i in range(start,n+1):
           
        #         comb.append(i)
        #         dfs(i+1, comb)
        #         comb.pop()
        # dfs(1,[])
        # return result
        