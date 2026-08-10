import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.replace(" ", "")
        s.lower()
        res = s.translate(s.maketrans('', '', string.punctuation)).replace(" ", "").lower()
        l = 0
        r = len(res) - 1
        while l < r:
            if res[l] != res[r]:
                return False
            l += 1
            r -= 1

        return True
            