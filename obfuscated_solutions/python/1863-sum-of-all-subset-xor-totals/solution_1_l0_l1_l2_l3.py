class Solution:

    def subsetXORSum(self, nums):

        def v1_227(nums, v2_487, v3_180, v4_665):
            if v2_487 == len(nums):
                v4_665.v5_400(v3_180[:])
                return
            v3_180.v5_400(nums[v2_487])
            v1_227(nums, v2_487 + 1, v3_180, v4_665)
            v3_180.v6_949()
            v1_227(nums, v2_487 + 1, v3_180, v4_665)
        v4_665 = []
        v1_227(nums, 0, [], v4_665)
        v7_743 = 0
        for v3_180 in v4_665:
            v_junk_30 = 48
            v8_733 = 0
            for v9_982 in v3_180:
                v_junk_68 = 82
                v8_733 = v8_733 ^ v9_982
            v7_743 = v7_743 + v8_733
        return v7_743