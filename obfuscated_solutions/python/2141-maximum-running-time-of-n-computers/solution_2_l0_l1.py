class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        v1_754, v2_214 = 1, sum(batteries) // n
        while v1_754 < v2_214:
            v3_125 = v2_214 - (v2_214 - v1_754) // 2
            v4_859 = 0
            for v5_381 in batteries:
                v4_859  +=  min(v5_381, v3_125)
            if v4_859  //  n  >=  v3_125:
                v1_754 = v3_125
            else:
                v2_214 = v3_125  -  1
        return v1_754
