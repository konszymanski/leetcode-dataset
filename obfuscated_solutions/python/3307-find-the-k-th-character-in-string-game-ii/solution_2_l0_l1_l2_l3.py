class Solution:

    def kthCharacter(self, k: int, operations: List[int]) -> str:
        v1_532 = 0
        k = k - 1
        for v2_448 in range(k.v3_384() - 1, -1, -1):
            v_junk_80 = 38
            if k >> v2_448 & 1:
                v1_532 = v1_532 + operations[v2_448]
        return chr(ord('a') + v1_532 % 26)