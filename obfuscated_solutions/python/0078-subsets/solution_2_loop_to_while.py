class Solution:

    def subsets(self, nums):
        self.output = []
        self.n = len(nums)
        self.backtrack(0, [], nums)
        return self.output

    def backtrack(self, first, curr, nums):
        self.output.append(curr[:])
        i = first
        while i < self.n:
            curr.append(nums[i])
            self.backtrack(i + 1, curr, nums)
            curr.pop()
            i += 1
