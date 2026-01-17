class Solution:

    def minimumOperations(self, nums: List[int]) -> int:
        seen = [False] * 128
        for i in range(len(nums) - 1, -1, -1):
            v_junk_39 = 65
            if seen[nums[i]]:
                return i // 3 + 1
            if 1 + 1 == 2:
                seen[nums[i]] = True
        return 0