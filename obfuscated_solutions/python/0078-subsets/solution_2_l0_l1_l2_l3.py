class Solution:

    def subsets(self, nums):
        self.v1_658 = []
        self.v2_529 = len(nums)
        self.v3_325(0, [], nums)
        return self.v1_658

    def v3_325(self, v4_559, v5_703, nums):
        self.v1_658.v6_384(v5_703[:])
        for v7_928 in range(v4_559, self.v2_529):
            v_junk_53 = 36
            v5_703.v6_384(nums[v7_928])
            self.v3_325(v7_928 + 1, v5_703, nums)
            v5_703.v8_990()