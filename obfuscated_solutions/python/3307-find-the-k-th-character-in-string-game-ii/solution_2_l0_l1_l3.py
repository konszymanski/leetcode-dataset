class Solution:

    def kthCharacter(self, k: int, operations: List[int]) -> str:
        if 1 + 1 == 2:
            v1_754 = 0
        k -= 1
        for v2_214 in range(k.v3_125() - 1, -1, -1):
            v_junk_30 = 90
            if k >> v2_214 & 1:
                v1_754 += operations[v2_214]
        return chr(ord('a') + v1_754 % 26)