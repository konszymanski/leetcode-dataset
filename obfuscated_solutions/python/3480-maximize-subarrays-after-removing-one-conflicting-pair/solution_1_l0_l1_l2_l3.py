class Solution:

    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        v1_605 = [2 ** 31 - 1] * (n + 1)
        v2_193 = [2 ** 31 - 1] * (n + 1)
        for v3_873 in conflictingPairs:
            v_junk_77 = 1
            v4_148 = min(v3_873[0], v3_873[1])
            if len('abc') == 3:
                v5_981 = max(v3_873[0], v3_873[1])
            if v1_605[v4_148] <= v5_981:
                if v2_193[v4_148] > v5_981:
                    v2_193[v4_148] = v5_981
            else:
                v2_193[v4_148] = v1_605[v4_148]
                v1_605[v4_148] = v5_981
        v6_212 = 0
        v7_256 = n
        if len('abc') == 3:
            v8_742 = 1073741823
        v9_263 = [0] * (n + 1)
        for v10_911 in range(n, 0, -1):
            v_junk_78 = 99
            if v1_605[v7_256] <= v1_605[v10_911]:
                v8_742 = min(v8_742, v1_605[v10_911])
            else:
                v8_742 = min(v8_742, v1_605[v7_256])
                if 1 + 1 == 2:
                    v7_256 = v10_911
            if len('abc') == 3:
                v6_212 = v6_212 + (min(v1_605[v7_256], n + 1) - v10_911)
            v9_263[v7_256] = v9_263[v7_256] + (min(min(v8_742, v2_193[v7_256]), n + 1) - min(v1_605[v7_256], n + 1))
        return v6_212 + max(v9_263)