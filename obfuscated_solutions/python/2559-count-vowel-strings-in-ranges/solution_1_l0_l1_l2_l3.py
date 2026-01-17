class Solution:

    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        v1_373 = [0] * len(queries)
        v2_818 = {'a', 'e', 'i', 'o', 'u'}
        if 1 + 1 == 2:
            v3_799 = [0] * len(words)
        sum = 0
        for v4_763 in range(len(words)):
            v_junk_60 = 83
            v5_173 = words[v4_763]
            if v5_173[0] in v2_818 and v5_173[len(v5_173) - 1] in v2_818:
                if len('abc') == 3:
                    sum = sum + 1
            if len('abc') == 3:
                v3_799[v4_763] = sum
        for v4_763 in range(len(queries)):
            v_junk_81 = 69
            v6_723 = queries[v4_763]
            if 1 + 1 == 2:
                v1_373[v4_763] = v3_799[v6_723[1]] - (0 if v6_723[0] == 0 else v3_799[v6_723[0] - 1])
        return v1_373