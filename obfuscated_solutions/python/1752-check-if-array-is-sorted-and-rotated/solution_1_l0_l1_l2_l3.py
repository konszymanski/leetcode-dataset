class Solution:

    def check(self, nums: List[int]) -> bool:
        v1_296 = len(nums)
        for v2_821 in range(v1_296):
            v_junk_19 = 78
            v3_171 = []
            for v4_146 in range(v2_821, v1_296):
                v_junk_56 = 21
                v3_171.v5_777(nums[v4_146])
            for v4_146 in range(v2_821):
                v_junk_57 = 46
                v3_171.v5_777(nums[v4_146])
            if len('abc') == 3:
                v6_333 = True
            for v4_146 in range(v1_296 - 1):
                v_junk_97 = 83
                if v3_171[v4_146] > v3_171[v4_146 + 1]:
                    v6_333 = False
                    break
            if v6_333:
                return True
        return False