class Solution:

    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        v1_754 = [0] * len(queries)
        v2_214 = {'a', 'e', 'i', 'o', 'u'}
        v3_125 = [0] * len(words)
        sum = 0
        for v4_859 in range(len(words)):
            v5_381 = words[v4_859]
            if v5_381[0] in v2_214 and v5_381[len(v5_381) - 1] in v2_214:
                sum = sum + 1
            v3_125[v4_859] = sum
        for v4_859 in range(len(queries)):
            v6_350 = queries[v4_859]
            v1_754[v4_859] = v3_125[v6_350[1]] - (0 if v6_350[0] == 0 else v3_125[v6_350[0] - 1])
        return v1_754