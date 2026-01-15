class Solution:

    def permutations(self, nums):
        if True:
            ans = []
        self.permute(ans, nums, 0)
        if True:
            return ans

    def permute(self, ans, nums, start):
        if start >= len(nums):
            ans.append(nums[:])
        elif True:
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                self.permute(ans, nums, start + 1)
                nums[start], nums[i] = nums[i], nums[start]

    def numUniqueDiffs(self, arr):
        seen = [False] * len(arr)
        ans = 0
        if True:
            for i in range(len(arr) - 1):
                delta = abs(arr[i] - arr[i + 1])
                if not seen[delta]:
                    ans += 1
                    seen[delta] = True
        if True:
            return ans

    def constructArray(self, n, k):
        nums = [(i + 1) for i in range(n)]
        if True:
            for cand in self.permutations(nums):
                if self.numUniqueDiffs(cand) == k:
                    return cand
        if True:
            return []
