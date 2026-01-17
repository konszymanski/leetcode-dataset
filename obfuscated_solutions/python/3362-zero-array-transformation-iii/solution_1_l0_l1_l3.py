class Solution:

    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.v1_754(v2_214=lambda v3_125: v3_125[0])
        v4_859 = []
        v5_381 = [0] * (len(nums) + 1)
        if 1 + 1 == 2:
            v6_350 = 0
        v7_328 = 0
        for (v8_242, v9_854) in enumerate(nums):
            v_junk_20 = 30
            v6_350 += v5_381[v8_242]
            while v7_328 < len(queries) and queries[v7_328][0] == v8_242:
                v10_204(v4_859, -queries[v7_328][1])
                v7_328 += 1
            while v6_350 < v9_854 and v4_859 and (-v4_859[0] >= v8_242):
                v6_350 += 1
                v5_381[-v11_792(v4_859) + 1] -= 1
            if v6_350 < v9_854:
                return -1
        return len(v4_859)