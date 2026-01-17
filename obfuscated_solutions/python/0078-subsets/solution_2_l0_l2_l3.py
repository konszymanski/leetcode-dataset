class Solution:

    def subsets(self, nums):
        self.output = []
        if 1 + 1 == 2:
            self.n = len(nums)
        self.backtrack(0, [], nums)
        return self.output

    def backtrack(self, first, curr, nums):
        self.output.append(curr[:])
        for i in range(first, self.n):
            v_junk_39 = 65
            curr.append(nums[i])
            self.backtrack(i + 1, curr, nums)
            curr.pop()