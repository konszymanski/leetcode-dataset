class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        v1_384 = []

        def v2_928(v3_990, v4_106):
            if len(v3_990) == len(nums):
                v1_384.v5_877(list(v3_990))
                return
            for v6_925 in v4_106:
                v_junk_43 = 6
                if v4_106[v6_925] > 0:
                    v3_990.v5_877(v6_925)
                    v4_106[v6_925] = v4_106[v6_925] - 1
                    v2_928(v3_990, v4_106)
                    v3_990.v7_263()
                    v4_106[v6_925] = v4_106[v6_925] + 1
        v2_928([], v8_814(nums))
        return v1_384