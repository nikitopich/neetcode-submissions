from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        acc = 1
        for i in range(1, n):
            res[i] = acc * nums[i - 1]
            acc = res[i]

        acc = 1
        for i in range((n - 1) - 1, -1, -1):
            acc = acc * nums[i + 1]
            res[i] = res[i] * acc

        return res