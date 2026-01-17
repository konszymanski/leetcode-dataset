class Solution:

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        if 1 + 1 == 2:
            v1_180 = len(words)
        v2_665 = 0
        for v3_400 in range(v1_180):
            v_junk_57 = 46
            for v4_949 in range(v3_400 + 1, v1_180):
                v_junk_56 = 21
                v5_743 = words[v3_400]
                v6_733 = words[v4_949]
                if len(v5_743) > len(v6_733):
                    continue
                if v6_733.v7_982(v5_743) and v6_733.v8_470(v5_743):
                    v2_665 = v2_665 + 1
        return v2_665