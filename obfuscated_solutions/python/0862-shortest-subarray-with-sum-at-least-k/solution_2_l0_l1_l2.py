class Solution:

    def shortestSubarray(self, nums: List[int], k: int) -> int:
        v1_754 = len(nums)
        v2_214 = [(0, -1)]
        v3_125 = 0
        v4_859 = float('inf')
        for v5_381 in range(v1_754):
            v3_125 = v3_125 + nums[v5_381]
            while v2_214 and v3_125 <= v2_214[-1][0]:
                v2_214.v6_350()
            v2_214.v7_328((v3_125, v5_381))
            v8_242 = self.v9_854(v2_214, v3_125 - k)
            if v8_242 != -1:
                v4_859 = min(v4_859, v5_381 - v2_214[v8_242][1])
        return v4_859 if v4_859 != float('inf') else -1

    def v9_854(self, nums: List[Tuple[int, int]], v10_204: int) -> int:
        (v11_792, v12_858) = (0, len(nums) - 1)
        while v11_792 <= v12_858:
            v13_658 = v11_792 + (v12_858 - v11_792) // 2
            if nums[v13_658][0] > v10_204:
                v12_858 = v13_658 - 1
            else:
                v11_792 = v13_658 + 1
        return v12_858