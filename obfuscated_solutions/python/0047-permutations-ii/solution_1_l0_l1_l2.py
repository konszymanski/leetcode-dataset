class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        v1_754 = []

        def v2_214(v3_125, v4_859):
            if len(v3_125) == len(nums):
                v1_754.v5_381(list(v3_125))
                return
            for v6_350 in v4_859:
                if v4_859[v6_350] > 0:
                    v3_125.v5_381(v6_350)
                    v4_859[v6_350] = v4_859[v6_350] - 1
                    v2_214(v3_125, v4_859)
                    v3_125.v7_328()
                    v4_859[v6_350] = v4_859[v6_350] + 1
        v2_214([], v8_242(nums))
        return v1_754