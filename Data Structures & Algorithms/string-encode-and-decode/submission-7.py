class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            s_len = ""
            while s[i] != '#':
                s_len += s[i]
                i += 1
            int_s_len = int(s_len)

            word = ""
            word_end_i = i + int_s_len + 1
            i += 1
            while i < word_end_i:
                word += s[i]
                i += 1
            result.append(word)
        
        return result
