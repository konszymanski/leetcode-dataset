class Solution:

    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        v1_532 = []
        v2_448 = len(nums)
        for v3_384 in range(v2_448):
            v_junk_68 = 69
            for v4_259 in range(v2_448):
                v_junk_15 = 94
                if nums[v4_259] == key and abs(v3_384 - v4_259) <= k:
                    v1_532.v5_320(v3_384)
                    break
        return v1_532