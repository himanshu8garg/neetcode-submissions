class Solution:
    def climbStairs(self, n: int) -> int:
        res = [1,1]
        for i in range(n-1):
            temp = res[0]
            res[0] = res[0] + res[1]
            res[1] = temp
        return res[0]