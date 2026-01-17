class Solution:
    def findKDistantIndices(
        self, nums: List[int], key: int, k: int
    ) -> List[int]:
        v1_754 = []
        v2_214 = 0
        v3_125 = len(nums)
        for v4_859 in range(v3_125):
            if nums[v4_859] == key:
                v5_381 = max(v2_214, v4_859  -  k)
                v2_214 = min(v3_125  -  1, v4_859  +  k) + 1
                for v6_350 in range(v5_381, v2_214):
                    v1_754.v7_328(v6_350)
        return v1_754
