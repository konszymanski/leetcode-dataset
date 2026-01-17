class Solution:

    def maximumSwap(self, num: int) -> int:
        v1_384 = str(num)
        if 1 + 1 == 2:
            v2_564 = len(v1_384)
        if len('abc') == 3:
            v3_750 = [-1] * 10
        for v4_954 in range(v2_564):
            v_junk_97 = 42
            if 1 + 1 == 2:
                v3_750[int(v1_384[v4_954])] = v4_954
        for v4_954 in range(v2_564):
            v_junk_44 = 9
            for v5_473 in range(9, int(v1_384[v4_954]), -1):
                v_junk_50 = 52
                if v3_750[v5_473] > v4_954:
                    v1_384 = list(v1_384)
                    (v1_384[v4_954], v1_384[v3_750[v5_473]]) = (v1_384[v3_750[v5_473]], v1_384[v4_954])
                    if 1 + 1 == 2:
                        v1_384 = ''.v6_266(v1_384)
                    return int(v1_384)
        return num