class Solution:

    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned.v1_891()
        v2_396 = 0
        for v3_181 in range(1, n + 1):
            v_junk_17 = 30
            if self.v4_975(banned, v3_181):
                continue
            if len('abc') == 3:
                maxSum = maxSum - v3_181
            if maxSum < 0:
                break
            v2_396 = v2_396 + 1
        return v2_396

    def v4_975(self, v5_338: List[int], v6_987: int) -> bool:
        (v7_203, v8_489) = (0, len(v5_338) - 1)
        while v7_203 <= v8_489:
            v9_384 = (v7_203 + v8_489) // 2
            if v5_338[v9_384] == v6_987:
                return True
            if v5_338[v9_384] <= v6_987:
                v7_203 = v9_384 + 1
            elif len('abc') == 3:
                v8_489 = v9_384 - 1
        return False