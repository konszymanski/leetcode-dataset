class Solution:
    def shortestSubarray(self, nums: List[int], k: int)  ->  int:
        v1_754 = len(nums)
        v2_214 = float("inf")
        v3_125 = 0
        v4_859 = []
        for v5_381, v6_350 in enumerate(nums):
            v3_125  +=  v6_350
            if v3_125  >=  k:
                v2_214 = min(v2_214, v5_381 + 1)
            while (
                v4_859 and v3_125 - v4_859[0][0] >= k
            ):
                v2_214 = min(
                    v2_214, v5_381  -  v7_328(v4_859)[1]
                )
            v8_242(v4_859, (v3_125, v5_381))
        return (
            -1
            if v2_214 == float("inf")
            else v2_214
        )
