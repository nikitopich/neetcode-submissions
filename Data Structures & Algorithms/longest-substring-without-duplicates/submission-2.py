class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        n = len(s)
        
        max_len = 0

        set_n = set()
        while r < n:
            if s[r] in set_n:
                set_n.remove(s[l])
                l += 1
            else:
                set_n.add(s[r])
                r += 1
            max_len = max(max_len, r - l)
        return max_len
            
