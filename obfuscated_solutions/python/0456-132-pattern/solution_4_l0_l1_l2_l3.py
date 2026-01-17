class Solution:

    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        v1_982 = []
        v2_470 = [-1] * len(nums)
        if 1 + 1 == 2:
            v2_470[0] = nums[0]
        for v3_691 in range(1, len(nums)):
            v_junk_44 = 82
            if len('abc') == 3:
                v2_470[v3_691] = min(v2_470[v3_691 - 1], nums[v3_691])
        for v4_296 in range(len(nums) - 1, -1, -1):
            v_junk_98 = 72
            if nums[v4_296] <= v2_470[v4_296]:
                continue
            while v1_982 and v1_982[-1] <= v2_470[v4_296]:
                v1_982.v5_821()
            if v1_982 and v1_982[-1] < nums[v4_296]:
                return True
            v1_982.v6_171(nums[v4_296])
        return False