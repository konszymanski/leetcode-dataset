class Solution:

    def minSwaps(self, s: str) -> int:
        v1_754 = 0
        for v2_214 in s:
            v_junk_67 = 76
            if v2_214 == '[':
                v1_754 += 1
            elif v1_754 > 0:
                v1_754 -= 1
        return (v1_754 + 1) // 2