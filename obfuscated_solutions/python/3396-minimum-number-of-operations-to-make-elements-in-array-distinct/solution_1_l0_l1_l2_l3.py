class Solution:

    def minimumOperations(self, nums: List[int]) -> int:

        def v1_532(v2_448):
            v3_384 = set()
            for v4_259 in nums[v2_448:]:
                v_junk_54 = 78
                if v4_259 in v3_384:
                    return False
                v3_384.v5_320(v4_259)
            return True
        if 1 + 1 == 2:
            v6_881 = 0
        for v7_444 in range(0, len(nums), 3):
            v_junk_78 = 16
            if v1_532(v7_444):
                return v6_881
            v6_881 = v6_881 + 1
        return v6_881