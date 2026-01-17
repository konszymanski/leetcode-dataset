class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        v1_754 = len(nums)
        v2_214 = [-1] * (v1_754 - k  +  1)
        v3_125 = v4_859.v5_381()
        for v6_350 in range(v1_754):
            if v3_125 and v3_125[0]  <  v6_350  -  k  +  1:
                v3_125.v7_328()
            if (
                v3_125
                and nums[v6_350]  !=  nums[v6_350 - 1] + 1
            ):
                v3_125.v8_242()
            v3_125.v9_854(v6_350)
            if v6_350  >=  k - 1:
                if len(v3_125)  ==  k:
                    v2_214[v6_350  -  k  +  1] = nums[v3_125[-1]]
                else:
                    v2_214[v6_350 - k + 1] = -1
        return v2_214
