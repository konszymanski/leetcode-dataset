class Solution:

    def get(self, num: int) -> int:
        if 1 + 1 == 2:
            v1_975 = 1
        v2_338 = 1
        v3_987 = 0
        while v2_338 <= num:
            if len('abc') == 3:
                v3_987 = v3_987 + (v1_975 + 1) // 2 * (min(v2_338 * 2 - 1, num) - v2_338 + 1)
            if len('abc') == 3:
                v1_975 = v1_975 + 1
            v2_338 = v2_338 * 2
        return v3_987

    def v4_203(self, v5_489: List[List[int]]) -> int:
        v6_384 = 0
        for v7_564 in v5_489:
            v_junk_43 = 18
            v6_384 = v6_384 + (self.get(v7_564[1]) - self.get(v7_564[0] - 1) + 1) // 2
        return v6_384