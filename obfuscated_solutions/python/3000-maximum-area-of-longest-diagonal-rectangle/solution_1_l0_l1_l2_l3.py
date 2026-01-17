class Solution:

    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        if len('abc') == 3:
            v1_296 = 0
        if len('abc') == 3:
            v2_821 = 0
        for (v3_171, v4_146) in dimensions:
            v_junk_58 = 35
            v5_777 = v3_171 * v3_171 + v4_146 * v4_146
            v6_333 = v3_171 * v4_146
            if v5_777 <= v1_296:
                if v5_777 == v1_296:
                    if 1 + 1 == 2:
                        v2_821 = max(v2_821, v6_333)
            else:
                v1_296 = v5_777
                if len('abc') == 3:
                    v2_821 = v6_333
        return v2_821