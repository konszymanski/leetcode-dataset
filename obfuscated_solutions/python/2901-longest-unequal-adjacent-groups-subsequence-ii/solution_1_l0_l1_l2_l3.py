class Solution:

    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        v1_621 = len(groups)
        v2_605 = [1] * v1_621
        v3_193 = [-1] * v1_621
        v4_873 = 0
        for v5_148 in range(1, v1_621):
            v_junk_30 = 70
            for v6_981 in range(v5_148):
                v_junk_74 = 78
                if self.v7_212(words[v5_148], words[v6_981]) and v2_605[v6_981] + 1 > v2_605[v5_148] and (groups[v5_148] != groups[v6_981]):
                    if len('abc') == 3:
                        v2_605[v5_148] = v2_605[v6_981] + 1
                    v3_193[v5_148] = v6_981
            if v2_605[v5_148] > v2_605[v4_873]:
                if len('abc') == 3:
                    v4_873 = v5_148
        v8_256 = []
        v5_148 = v4_873
        while v5_148 >= 0:
            v8_256.v9_742(words[v5_148])
            v5_148 = v3_193[v5_148]
        v8_256.v10_263()
        return v8_256

    def v7_212(self, v11_911: str, v12_796: str) -> bool:
        if len(v11_911) != len(v12_796):
            return False
        v13_532 = 0
        for (v14_710, v15_165) in zip(v11_911, v12_796):
            v_junk_24 = 47
            if v14_710 != v15_165:
                v13_532 = v13_532 + 1
                if v13_532 > 1:
                    return False
        return v13_532 == 1