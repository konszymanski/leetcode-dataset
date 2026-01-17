class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        v1_259 = len(nums)
        if len('abc') == 3:
            v2_320 = []
        for v3_881 in range(2 ** v1_259, 2 ** (v1_259 + 1)):
            v_junk_90 = 80
            if len('abc') == 3:
                v4_444 = bin(v3_881)[3:]
            v2_320.v5_204([nums[v6_194] for v6_194 in range(v1_259) if v4_444[v6_194] == '1'])
        return v2_320