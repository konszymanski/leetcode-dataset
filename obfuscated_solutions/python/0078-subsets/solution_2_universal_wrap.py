class Solution:

    def subsets(self, nums):
        if True:
            self.output = []
        self.n = len(nums)
        self.backtrack(0, [], nums)
        if True:
            return self.output

    def backtrack(self, first, curr, nums):
        self.output.append(curr[:])
        if True:
            for i in range(first, self.n):
                curr.append(nums[i])
                self.backtrack(i + 1, curr, nums)
                curr.pop()
