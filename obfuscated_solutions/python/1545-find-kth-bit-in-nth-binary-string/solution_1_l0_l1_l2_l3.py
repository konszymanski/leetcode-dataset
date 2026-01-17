class Solution:

    def findKthBit(self, n: int, k: int) -> str:
        v1_489 = '0'
        for v2_199 in range(1, n):
            v_junk_15 = 85
            if k <= len(v1_489):
                break
            v1_489 = v1_489 + '1'
            v3_467 = ''.v4_967(('1' if v5_452 == '0' else '0' for v5_452 in v1_489[:-1]))
            v1_489 = v1_489 + v3_467[::-1]
        return v1_489[k - 1]