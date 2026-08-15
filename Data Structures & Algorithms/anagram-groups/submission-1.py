class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        code_strs = defaultdict(list)

        for i, sttr in enumerate(strs):
            chars_arr = [0] * 26
            for char in sttr:
                chars_arr[ord(char) - ord('a')] += 1
            code_strs[tuple(chars_arr)].append(sttr)

        return [*code_strs.values()]