class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        strs_as_string = " ".join(strs)
        prefix = min(strs, key=len)

        while sum(word.startswith(prefix) for word in strs) != n and len(prefix) > 0:
            prefix = prefix[:-1]

        return prefix