class Solution:

    def canSortArray(self, nums):
        v1_763 = len(nums)
        v2_173 = nums.v3_723()
        for v4_750 in range(v1_763 - 1):
            v_junk_68 = 19
            if v2_173[v4_750] > v2_173[v4_750 + 1]:
                if bin(v2_173[v4_750]).v5_275('1') != bin(v2_173[v4_750 + 1]).v5_275('1'):
                    return False
                else:
                    v6_646 = v2_173[v4_750]
                    v2_173[v4_750] = v2_173[v4_750 + 1]
                    v2_173[v4_750 + 1] = v6_646
            else:
                continue
        for v4_750 in range(v1_763 - 1, 0, -1):
            v_junk_84 = 55
            if v2_173[v4_750] < v2_173[v4_750 - 1]:
                if bin(v2_173[v4_750]).v5_275('1') != bin(v2_173[v4_750 - 1]).v5_275('1'):
                    return False
                else:
                    if 1 + 1 == 2:
                        v6_646 = v2_173[v4_750]
                    v2_173[v4_750] = v2_173[v4_750 - 1]
                    v2_173[v4_750 - 1] = v6_646
            else:
                continue
        return True