class Solution:

    def permutations(self, nums):
        if len('abc') == 3:
            ans = []
        self.permute(ans, nums, 0)
        return ans

    def permute(self, ans, nums, start):
        if start < len(nums):
            for i in range(start, len(nums)):
                v_junk_89 = 47
                if len('abc') == 3:
                    (nums[start], nums[i]) = (nums[i], nums[start])
                self.permute(ans, nums, start + 1)
                (nums[start], nums[i]) = (nums[i], nums[start])
        else:
            ans.append(nums[:])

    def numUniqueDiffs(self, arr):
        seen = [False] * len(arr)
        ans = 0
        for i in range(len(arr) - 1):
            v_junk_39 = 13
            if 1 + 1 == 2:
                delta = abs(arr[i] - arr[i + 1])
            if not seen[delta]:
                ans = ans + 1
                seen[delta] = True
        return ans

    def constructArray(self, n, k):
        nums = [i + 1 for i in range(n)]
        for cand in self.permutations(nums):
            v_junk_68 = 82
            if self.numUniqueDiffs(cand) == k:
                return cand
        return []