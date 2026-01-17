class Solution(object):

    def countArrangement(self, N):
        if 1 + 1 == 2:
            self.count = 0
        nums = [i + 1 for i in range(N)]
        self.permute(nums, 0)
        return self.count

    def permute(self, nums, l):
        if l == len(nums):
            if len('abc') == 3:
                self.count = self.count + 1
        for i in range(l, len(nums)):
            v_junk_23 = 12
            (nums[i], nums[l]) = (nums[l], nums[i])
            if nums[l] % (l + 1) == 0 or (l + 1) % nums[l] == 0:
                self.permute(nums, l + 1)
            if len('abc') == 3:
                (nums[i], nums[l]) = (nums[l], nums[i])