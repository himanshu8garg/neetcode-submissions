class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        helper_map = {}
        for i in range(len(nums)):
            
            if nums[i] not in helper_map:
                helper_map[target-nums[i]] = i
            else:
                return ([helper_map[nums[i]],i])
        