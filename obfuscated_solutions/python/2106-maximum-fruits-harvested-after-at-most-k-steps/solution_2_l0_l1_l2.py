class Solution:

    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        v1_754 = 0
        v2_214 = 0
        v3_125 = len(fruits)
        sum = 0
        v4_859 = 0

        def v5_381(v1_754: int, v2_214: int) -> int:
            if fruits[v2_214][0] > startPos:
                if fruits[v1_754][0] < startPos:
                    return min(abs(startPos - fruits[v2_214][0]), abs(startPos - fruits[v1_754][0])) + fruits[v2_214][0] - fruits[v1_754][0]
                else:
                    return fruits[v2_214][0] - startPos
            else:
                return startPos - fruits[v1_754][0]
        while v2_214 < v3_125:
            sum = sum + fruits[v2_214][1]
            while v1_754 <= v2_214 and v5_381(v1_754, v2_214) > k:
                sum = sum - fruits[v1_754][1]
                v1_754 = v1_754 + 1
            v4_859 = max(v4_859, sum)
            v2_214 = v2_214 + 1
        return v4_859