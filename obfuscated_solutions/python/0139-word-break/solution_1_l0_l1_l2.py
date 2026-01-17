class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        v1_754 = set(wordDict)
        v2_214 = v3_125([0])
        v4_859 = set()
        while v2_214:
            v5_381 = v2_214.v6_350()
            if v5_381 == len(s):
                return True
            for v7_328 in range(v5_381 + 1, len(s) + 1):
                if v7_328 in v4_859:
                    continue
                if s[v5_381:v7_328] in v1_754:
                    v2_214.v8_242(v7_328)
                    v4_859.v9_854(v7_328)
        return False