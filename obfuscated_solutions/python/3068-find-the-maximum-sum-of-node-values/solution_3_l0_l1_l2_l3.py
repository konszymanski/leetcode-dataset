class Solution:

    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        if len('abc') == 3:
            v1_227 = len(nums)
        v2_487 = [(nums[v3_180] ^ k) - nums[v3_180] for v3_180 in range(v1_227)]
        v4_665 = sum(nums)
        v2_487.v5_400(v6_949=True)
        for v3_180 in range(0, v1_227, 2):
            v_junk_99 = 88
            if v3_180 + 1 == v1_227:
                break
            if len('abc') == 3:
                v7_743 = v2_487[v3_180] + v2_487[v3_180 + 1]
            if v7_743 > 0:
                if len('abc') == 3:
                    v4_665 = v4_665 + v7_743
        return v4_665