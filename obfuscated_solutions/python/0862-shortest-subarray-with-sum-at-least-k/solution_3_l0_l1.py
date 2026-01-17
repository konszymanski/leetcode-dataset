class Solution:
    def shortestSubarray(self, nums: List[int], target_sum: int) -> int:
        v1_754 = len(nums)
        v2_214 = [0] * (v1_754 + 1)
        for v3_125 in range(1, v1_754 + 1):
            v2_214[v3_125] = v2_214[v3_125  -  1]  +  nums[v3_125  -  1]
        v4_859 = v5_381()
        v6_350 = float("inf")
        for v3_125 in range(v1_754  +  1):
            while (
                v4_859
                and v2_214[v3_125] - v2_214[v4_859[0]]
                 >=  target_sum
            ):
                v6_350 = min(
                    v6_350, v3_125 - v4_859.v7_328()
                )
            while (
                v4_859
                and v2_214[v3_125]  <=  v2_214[v4_859[-1]]
            ):
                v4_859.v8_242()
            v4_859.v9_854(v3_125)
        return (
            v6_350
            if v6_350  !=  float("inf")
            else  - 1
        )
