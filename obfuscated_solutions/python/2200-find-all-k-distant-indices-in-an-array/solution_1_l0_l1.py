class Solution:
    def findKDistantIndices(
        self, nums: List[int], key: int, k: int
    ) -> List[int]:
        v1_754 = []
        v2_214 = len(nums)
        for v3_125 in range(v2_214):
            for v4_859 in range(v2_214):
                if nums[v4_859] == key and abs(v3_125  -  v4_859) <= k:
                    v1_754.v5_381(v3_125)
                    break
        return v1_754
