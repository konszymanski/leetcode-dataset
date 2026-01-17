class Solution:

    def minimumOperations(self, nums: List[int]) -> int:

        def v1_754(v2_214):
            v3_125 = set()
            for v4_859 in nums[v2_214:]:
                if v4_859 in v3_125:
                    return False
                v3_125.v5_381(v4_859)
            return True
        v6_350 = 0
        for v7_328 in range(0, len(nums), 3):
            if v1_754(v7_328):
                return v6_350
            v6_350 = v6_350 + 1
        return v6_350