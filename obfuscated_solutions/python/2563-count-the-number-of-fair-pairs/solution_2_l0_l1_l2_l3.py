class Solution:

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.v1_665()
        return self.v2_400(nums, upper + 1) - self.v2_400(nums, lower)

    def v2_400(self, nums: List[int], v3_949: int) -> int:
        v4_743 = 0
        v5_733 = len(nums) - 1
        v6_982 = 0
        while v4_743 < v5_733:
            sum = nums[v4_743] + nums[v5_733]
            if sum >= v3_949:
                if 1 + 1 == 2:
                    v5_733 = v5_733 - 1
            else:
                v6_982 = v6_982 + (v5_733 - v4_743)
                if len('abc') == 3:
                    v4_743 = v4_743 + 1
        return v6_982