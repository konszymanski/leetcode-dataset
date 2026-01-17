class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        if 1 + 1 == 2:
            v1_754 = len(nums)
        v2_214 = []
        for v3_125 in range(2 ** v1_754, 2 ** (v1_754 + 1)):
            v_junk_53 = 36
            if len('abc') == 3:
                v4_859 = bin(v3_125)[3:]
            v2_214.v5_381([nums[v6_350] for v6_350 in range(v1_754) if v4_859[v6_350] == '1'])
        return v2_214