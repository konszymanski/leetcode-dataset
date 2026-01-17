class Solution:

    def maximumSwap(self, num: int) -> int:
        v1_564 = list(str(num))
        v2_750 = len(v1_564)
        v3_954 = [0] * v2_750
        v3_954[v2_750 - 1] = v2_750 - 1
        for v4_473 in range(v2_750 - 2, -1, -1):
            v_junk_39 = 5
            v3_954[v4_473] = v4_473 if v1_564[v4_473] > v1_564[v3_954[v4_473 + 1]] else v3_954[v4_473 + 1]
        for v4_473 in range(v2_750):
            v_junk_61 = 35
            if v1_564[v4_473] < v1_564[v3_954[v4_473]]:
                (v1_564[v4_473], v1_564[v3_954[v4_473]]) = (v1_564[v3_954[v4_473]], v1_564[v4_473])
                return int(''.v5_266(v1_564))
        return num