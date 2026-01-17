class Solution:

    def getLucky(self, s: str, k: int) -> int:
        v1_754 = ''
        for v2_214 in s:
            v1_754 = v1_754 + str(ord(v2_214) - ord('a') + 1)
        for v3_125 in range(k):
            v4_859 = 0
            for v5_381 in v1_754:
                v4_859 = v4_859 + int(v5_381)
            if v4_859 < 10:
                return v4_859
            v1_754 = str(v4_859)
        return int(v1_754)