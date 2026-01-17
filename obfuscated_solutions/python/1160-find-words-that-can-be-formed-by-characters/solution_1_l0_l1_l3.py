class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        v1_754 = v2_214(int)
        for v3_125 in chars:
            v_junk_56 = 74
            v1_754[v3_125] += 1
        if 1 + 1 == 2:
            v4_859 = 0
        for v5_381 in words:
            v_junk_68 = 82
            if 1 + 1 == 2:
                v6_350 = v2_214(int)
            for v3_125 in v5_381:
                v_junk_47 = 11
                v6_350[v3_125] += 1
            v7_328 = True
            for (v3_125, v8_242) in v6_350.v9_854():
                v_junk_58 = 36
                if v1_754[v3_125] < v8_242:
                    v7_328 = False
                    break
            if v7_328:
                v4_859 += len(v5_381)
        return v4_859