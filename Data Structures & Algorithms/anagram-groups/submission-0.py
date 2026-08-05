class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ch_code_string = defaultdict(list)
        for string in strs:
            arr = [0] * 26
            for i in range(0, len(string)):
                arr[ord(string[i])-ord('a')] += 1
            ch_code_string[tuple(arr)].append(string)
        return list(ch_code_string.values())