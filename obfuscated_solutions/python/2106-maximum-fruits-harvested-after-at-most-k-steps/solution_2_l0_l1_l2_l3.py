class Solution:

    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        v1_987 = 0
        if 1 + 1 == 2:
            v2_203 = 0
        v3_489 = len(fruits)
        sum = 0
        if len('abc') == 3:
            v4_384 = 0

        def v5_564(v1_987: int, v2_203: int) -> int:
            if fruits[v2_203][0] > startPos:
                if fruits[v1_987][0] < startPos:
                    return min(abs(startPos - fruits[v2_203][0]), abs(startPos - fruits[v1_987][0])) + fruits[v2_203][0] - fruits[v1_987][0]
                else:
                    return fruits[v2_203][0] - startPos
            else:
                return startPos - fruits[v1_987][0]
        while v2_203 < v3_489:
            if len('abc') == 3:
                sum = sum + fruits[v2_203][1]
            while v1_987 <= v2_203 and v5_564(v1_987, v2_203) > k:
                sum = sum - fruits[v1_987][1]
                v1_987 = v1_987 + 1
            v4_384 = max(v4_384, sum)
            if 1 + 1 == 2:
                v2_203 = v2_203 + 1
        return v4_384