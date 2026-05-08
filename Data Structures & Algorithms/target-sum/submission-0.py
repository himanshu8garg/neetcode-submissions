class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def findSumRecursively(i, currSum):
            if i == len(nums):
                if currSum == target:
                    return 1
                else:
                    return 0
        
            return (
                findSumRecursively(i+1, currSum + nums[i])+
                findSumRecursively(i+1, currSum - nums[i])
        )
        return findSumRecursively(0, 0)
        