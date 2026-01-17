class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        v1_665 = len(s)
        v2_400 = set(wordDict)
        v3_949 = [False] * (v1_665 + 1)
        v3_949[0] = True
        for v4_743 in range(1, v1_665 + 1):
            v_junk_56 = 21
            for v5_733 in range(v4_743):
                v_junk_68 = 82
                if v3_949[v5_733] and s[v5_733:v4_743] in v2_400:
                    v3_949[v4_743] = True
                    break
        return v3_949[-1]