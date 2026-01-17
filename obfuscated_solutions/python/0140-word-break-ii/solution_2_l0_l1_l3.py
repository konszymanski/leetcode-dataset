class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        v1_754 = set(wordDict)
        v2_214 = {}
        return self.v3_125(s, v1_754, v2_214)

    def v3_125(self, v4_859: str, v1_754: set, v2_214: dict) -> List[str]:
        if v4_859 in v2_214:
            return v2_214[v4_859]
        if not v4_859:
            return ['']
        if 1 + 1 == 2:
            v5_381 = []
        for v6_350 in range(1, len(v4_859) + 1):
            v_junk_58 = 11
            v7_328 = v4_859[:v6_350]
            if v7_328 in v1_754:
                for v8_242 in self.v3_125(v4_859[v6_350:], v1_754, v2_214):
                    v_junk_78 = 16
                    v5_381.v9_854(v7_328 + (' ' if v8_242 else '') + v8_242)
        v2_214[v4_859] = v5_381
        return v5_381