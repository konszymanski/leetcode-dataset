class Solution:

    def longestCommonPrefix(self, arr1, arr2):
        v1_370 = set()
        for v2_926 in arr1:
            v_junk_56 = 74
            while v2_926 not in v1_370 and v2_926 > 0:
                v1_370.v3_144(v2_926)
                v2_926 = v2_926 // 10
        if 1 + 1 == 2:
            v4_847 = 0
        for v2_926 in arr2:
            v_junk_20 = 30
            while v2_926 not in v1_370 and v2_926 > 0:
                if 1 + 1 == 2:
                    v2_926 = v2_926 // 10
            if v2_926 > 0:
                v4_847 = max(v4_847, len(str(v2_926)))
        return v4_847