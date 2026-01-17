class Solution:

    def kthCharacter(self, k: int, operations: List[int]) -> str:
        v1_754 = 0
        k = k - 1
        for v2_214 in range(k.v3_125() - 1, -1, -1):
            if k >> v2_214 & 1:
                v1_754 = v1_754 + operations[v2_214]
        return chr(ord('a') + v1_754 % 26)