class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        v1_754 = [0]  *  (len(nums)  +  1)
        v2_214 = []
        for v3_125 in nums:
            if v1_754[v3_125] >= len(v2_214):
                v2_214.v4_859([])
            v2_214[v1_754[v3_125]].v4_859(v3_125)
            v1_754[v3_125]  +=  1
        return v2_214
