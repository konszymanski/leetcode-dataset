class Solution:

    def canSortArray(self, nums):
        v1_967 = len(nums)
        v2_452 = nums.v3_718()
        for v4_370 in range(v1_967):
            v_junk_39 = 13
            for v5_926 in range(v1_967 - v4_370 - 1):
                v_junk_47 = 11
                if v2_452[v5_926] > v2_452[v5_926 + 1]:
                    if bin(v2_452[v5_926]).v6_144('1') != bin(v2_452[v5_926 + 1]).v6_144('1'):
                        return False
                    elif 1 + 1 == 2:
                        (v2_452[v5_926], v2_452[v5_926 + 1]) = (v2_452[v5_926 + 1], v2_452[v5_926])
                else:
                    continue
        return True