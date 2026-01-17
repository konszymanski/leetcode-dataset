class Solution:
    def countPrefixSuffixPairs(self, words: List[str])  ->  int:
        v1_754 = len(words)
        v2_214 = 0
        for v3_125 in range(v1_754):
            for v4_859 in range(v3_125  +  1, v1_754):
                v5_381 = words[v3_125]
                v6_350 = words[v4_859]
                if len(v5_381) > len(v6_350):
                    continue
                if v6_350.v7_328(v5_381) and v6_350.v8_242(v5_381):
                    v2_214  +=  1
        return v2_214
