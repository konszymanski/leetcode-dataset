class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        v1_754 = v2_214(int)
        for v3_125 in chars:
            v1_754[v3_125]  +=  1
        v4_859 = 0
        for v5_381 in words:
            v6_350 = v2_214(int)
            for v3_125 in v5_381:
                v6_350[v3_125]  +=  1
            v7_328 = True
            for v3_125, v8_242 in v6_350.v9_854():
                if v1_754[v3_125] < v8_242:
                    v7_328 = False
                    break
            if v7_328:
                v4_859  +=  len(v5_381)
        return v4_859
