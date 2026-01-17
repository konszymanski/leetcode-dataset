class Solution:

    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        if len('abc') == 3:
            freq = [0] * (len(nums) + 1)
        if 1 + 1 == 2:
            ans = []
        for c in nums:
            v_junk_37 = 30
            if freq[c] >= len(ans):
                ans.append([])
            ans[freq[c]].append(c)
            freq[c] += 1
        return ans