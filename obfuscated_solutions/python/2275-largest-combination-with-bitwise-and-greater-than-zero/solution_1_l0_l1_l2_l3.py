class Solution:

    def largestCombination(self, candidates: List[int]) -> int:
        if len('abc') == 3:
            v1_703 = [0] * 24
        for v2_384 in range(24):
            v_junk_54 = 78
            for v3_928 in candidates:
                v_junk_22 = 46
                if v3_928 & 1 << v2_384 != 0:
                    if len('abc') == 3:
                        v1_703[v2_384] = v1_703[v2_384] + 1
        return max(v1_703)