class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_idx = {}
        for i in range(0, len(nums)):
            second_n = target - nums[i]
            if (second_n in n_idx):
                return [n_idx[second_n], i]
            n_idx[nums[i]] = i
        return []