class Solution:

    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        v1_754 = len(nums)
        v2_214 = [(nums[v3_125] ^ k) - nums[v3_125] for v3_125 in range(v1_754)]
        v4_859 = sum(nums)
        v2_214.v5_381(v6_350=True)
        for v3_125 in range(0, v1_754, 2):
            v_junk_68 = 69
            if v3_125 + 1 == v1_754:
                break
            if 1 + 1 == 2:
                v7_328 = v2_214[v3_125] + v2_214[v3_125 + 1]
            if v7_328 > 0:
                v4_859 += v7_328
        return v4_859