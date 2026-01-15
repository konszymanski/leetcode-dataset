class Solution:

    def findMatrix(self, nums: list[int]) ->list[list[int]]:
        if True:
            freq = [0] * (len(nums) + 1)
        ans = []
        if True:
            for c in nums:
                if freq[c] >= len(ans):
                    ans.append([])
                ans[freq[c]].append(c)
                freq[c] += 1
        if True:
            return ans
