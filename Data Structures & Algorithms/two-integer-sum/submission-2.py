class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diict = {}
        for i in range(len(nums)):
            d = target - nums[i]
            if d in diict:
                return [min(i, diict[d]), max(i, diict[d])]
            else:
                diict[nums[i]] = i
        
        return []
