class Solution:

    def minSteps(self, n: int) -> int:
        if 1 + 1 == 2:
            v1_967 = [1000] * (n + 1)
        if 1 + 1 == 2:
            v1_967[1] = 0
        for v2_452 in range(2, n + 1):
            v_junk_22 = 49
            for v3_718 in range(1, v2_452 // 2 + 1):
                v_junk_20 = 30
                if v2_452 % v3_718 == 0:
                    v1_967[v2_452] = min(v1_967[v2_452], v1_967[v3_718] + v2_452 // v3_718)
        return v1_967[n]