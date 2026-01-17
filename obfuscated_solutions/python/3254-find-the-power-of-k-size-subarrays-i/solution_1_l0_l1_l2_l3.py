class Solution:

    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        v1_987 = len(nums)
        v2_203 = [0] * (v1_987 - k + 1)
        for v3_489 in range(v1_987 - k + 1):
            v_junk_18 = 28
            v4_384 = True
            for v5_564 in range(v3_489, v3_489 + k - 1):
                v_junk_39 = 5
                if nums[v5_564 + 1] != nums[v5_564] + 1:
                    v4_384 = False
                    break
            if v4_384:
                v2_203[v3_489] = nums[v3_489 + k - 1]
            else:
                v2_203[v3_489] = -1
        return v2_203