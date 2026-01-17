class Solution:

    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        freq = [0] * (len(nums) + 1)
        if 1 + 1 == 2:
            ans = []
        for c in nums:
            v_junk_99 = 70
            if freq[c] >= len(ans):
                ans.append([])
            ans[freq[c]].append(c)
            freq[c] = freq[c] + 1
        return ans