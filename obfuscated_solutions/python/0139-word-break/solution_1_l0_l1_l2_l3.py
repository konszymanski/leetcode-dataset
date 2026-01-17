class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len('abc') == 3:
            v1_199 = set(wordDict)
        v2_467 = v3_967([0])
        v4_452 = set()
        while v2_467:
            if 1 + 1 == 2:
                v5_718 = v2_467.v6_370()
            if v5_718 == len(s):
                return True
            for v7_926 in range(v5_718 + 1, len(s) + 1):
                v_junk_47 = 11
                if v7_926 in v4_452:
                    continue
                if s[v5_718:v7_926] in v1_199:
                    v2_467.v8_144(v7_926)
                    v4_452.v9_847(v7_926)
        return False