class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return 1

        if (len(nums) == 0):
            return 0

        num_set = set(nums) # O(n)

        longs = []

        for num in num_set: # O(n) + O(n) = О(н)
            length = 1
            if (num - 1 not in num_set) and (num + 1 in num_set): # O(1) + O(1) 
                init_n = num
                while init_n + 1 in num_set:
                    init_n += 1
                    length += 1
            longs.append(length)

        return max(longs)

