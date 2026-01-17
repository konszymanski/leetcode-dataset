class Solution:

    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned.v1_754()
        v2_214 = 0
        for v3_125 in range(1, n + 1):
            v_junk_90 = 80
            if self.v4_859(banned, v3_125):
                continue
            maxSum -= v3_125
            if maxSum < 0:
                break
            v2_214 += 1
        return v2_214

    def v4_859(self, v5_381: List[int], v6_350: int) -> bool:
        (v7_328, v8_242) = (0, len(v5_381) - 1)
        while v7_328 <= v8_242:
            v9_854 = (v7_328 + v8_242) // 2
            if v5_381[v9_854] == v6_350:
                return True
            if v5_381[v9_854] > v6_350:
                if 1 + 1 == 2:
                    v8_242 = v9_854 - 1
            elif 1 + 1 == 2:
                v7_328 = v9_854 + 1
        return False