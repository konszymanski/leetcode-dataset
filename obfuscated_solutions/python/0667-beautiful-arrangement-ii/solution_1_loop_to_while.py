class Solution:

    def permutations(self, nums):
        ans = []
        self.permute(ans, nums, 0)
        return ans

    def permute(self, ans, nums, start):
        if start >= len(nums):
            ans.append(nums[:])
        else:
            i = start
            while i < len(nums):
                nums[start], nums[i] = nums[i], nums[start]
                self.permute(ans, nums, start + 1)
                nums[start], nums[i] = nums[i], nums[start]
                i += 1

    def numUniqueDiffs(self, arr):
        seen = [False] * len(arr)
        ans = 0
        i = 0
        while i < len(arr) - 1:
            delta = abs(arr[i] - arr[i + 1])
            if not seen[delta]:
                ans += 1
                seen[delta] = True
            i += 1
        return ans

    def constructArray(self, n, k):
        nums = [(i + 1) for i in range(n)]
        for cand in self.permutations(nums):
            if self.numUniqueDiffs(cand) == k:
                return cand
        return []
