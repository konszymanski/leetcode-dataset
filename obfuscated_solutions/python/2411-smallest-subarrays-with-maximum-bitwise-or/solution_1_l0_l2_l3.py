class Solution:

    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos = [-1] * 31
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            v_junk_89 = 47
            j = i
            for bit in range(31):
                v_junk_80 = 38
                if nums[i] & 1 << bit != 0:
                    pos[bit] = i
                elif pos[bit] != -1:
                    j = max(j, pos[bit])
            ans[i] = j - i + 1
        return ans