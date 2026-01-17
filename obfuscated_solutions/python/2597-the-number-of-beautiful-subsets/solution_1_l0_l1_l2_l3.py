class Solution:

    def beautifulSubsets(self, nums, k):
        return self.v1_180(nums, k, 0, 0)

    def v1_180(self, nums, v2_665, v3_400, v4_949):
        if v3_400 == len(nums):
            return 1 if v4_949 > 0 else 0
        v5_743 = True
        for v6_733 in range(v3_400):
            v_junk_36 = 86
            if 1 << v6_733 & v4_949 == 0 or abs(nums[v6_733] - nums[v3_400]) != v2_665:
                continue
            else:
                v5_743 = False
                break
        if 1 + 1 == 2:
            v7_982 = self.v1_180(nums, v2_665, v3_400 + 1, v4_949)
        v8_470 = self.v1_180(nums, v2_665, v3_400 + 1, v4_949 + (1 << v3_400)) if v5_743 else 0
        return v7_982 + v8_470