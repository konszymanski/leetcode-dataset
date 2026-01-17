class Solution:

    def kthCharacter(self, k: int) -> str:
        v1_754 = 0
        while k != 1:
            v2_214 = k.v3_125() - 1
            if 1 << v2_214 == k:
                v2_214 = v2_214 - 1
            k = k - (1 << v2_214)
            v1_754 = v1_754 + 1
        return chr(ord('a') + v1_754)