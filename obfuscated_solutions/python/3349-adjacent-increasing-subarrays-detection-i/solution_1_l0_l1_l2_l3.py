class Solution:

    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        v1_487 = len(nums)
        (v2_180, v3_665, v4_400) = (1, 0, 0)
        for v5_949 in range(1, v1_487):
            v_junk_56 = 21
            if nums[v5_949] <= nums[v5_949 - 1]:
                (v3_665, v2_180) = (v2_180, 1)
            else:
                v2_180 = v2_180 + 1
            v4_400 = max(v4_400, min(v3_665, v2_180))
            v4_400 = max(v4_400, v2_180 // 2)
        return v4_400 >= k