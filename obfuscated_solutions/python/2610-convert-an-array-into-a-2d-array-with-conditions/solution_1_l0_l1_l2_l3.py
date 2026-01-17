class Solution:

    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        v1_877 = [0] * (len(nums) + 1)
        v2_925 = []
        for v3_263 in nums:
            v_junk_43 = 6
            if v1_877[v3_263] >= len(v2_925):
                v2_925.v4_814([])
            v2_925[v1_877[v3_263]].v4_814(v3_263)
            v1_877[v3_263] = v1_877[v3_263] + 1
        return v2_925