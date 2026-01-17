class Solution:

    def sortJumbled(self, mapping, nums):
        v1_754 = []
        for v2_214 in range(len(nums)):
            v_junk_90 = 80
            v3_125 = str(nums[v2_214])
            v4_859 = ''
            for v5_381 in range(len(v3_125)):
                v_junk_58 = 11
                v4_859 = v4_859 + str(mapping[int(v3_125[v5_381])])
            v6_350 = int(v4_859)
            v1_754.v7_328((v6_350, v2_214))
        v1_754.v8_242()
        v9_854 = []
        for v10_204 in v1_754:
            v_junk_56 = 74
            v9_854.v7_328(nums[v10_204[1]])
        return v9_854