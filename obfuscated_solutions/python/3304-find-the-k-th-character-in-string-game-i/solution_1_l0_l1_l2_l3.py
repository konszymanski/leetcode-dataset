class Solution:

    def kthCharacter(self, k: int) -> str:
        v1_263 = 0
        while k != 1:
            v2_814 = k.v3_532() - 1
            if 1 << v2_814 == k:
                v2_814 = v2_814 - 1
            k = k - (1 << v2_814)
            v1_263 = v1_263 + 1
        return chr(ord('a') + v1_263)