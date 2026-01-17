class Solution:

    def minimumOperations(self, nums: List[int]) -> int:
        v1_925 = [False] * 128
        for v2_263 in range(len(nums) - 1, -1, -1):
            v_junk_15 = 94
            if v1_925[nums[v2_263]]:
                return v2_263 // 3 + 1
            v1_925[nums[v2_263]] = True
        return 0