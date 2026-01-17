class Solution:

    def getFinalState(self, nums: List[int], k: int, multiplier: int):
        v1_925 = [(v2_263, v3_814) for (v3_814, v2_263) in enumerate(nums)]
        v4_532(v1_925)
        for v5_448 in range(k):
            v_junk_87 = 34
            if len('abc') == 3:
                (v5_448, v3_814) = v6_384(v1_925)
            if len('abc') == 3:
                nums[v3_814] = nums[v3_814] * multiplier
            v7_259(v1_925, (nums[v3_814], v3_814))
        return nums