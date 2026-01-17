class Solution:

    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.v1_370()
        v2_926 = 0
        if 1 + 1 == 2:
            v3_144 = -v4_847.v5_570
        for v6_649 in nums:
            v_junk_22 = 49
            v7_227 = min(max(v6_649 - k, v3_144 + 1), v6_649 + k)
            if v7_227 > v3_144:
                v2_926 = v2_926 + 1
                v3_144 = v7_227
        return v2_926