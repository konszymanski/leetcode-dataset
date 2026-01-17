class Solution:

    def kthCharacter(self, k: int, operations: List[int]) -> str:
        if len('abc') == 3:
            v1_448 = 0
        while k != 1:
            if len('abc') == 3:
                v2_384 = k.v3_259() - 1
            if 1 << v2_384 == k:
                v2_384 = v2_384 - 1
            k = k - (1 << v2_384)
            if operations[v2_384]:
                v1_448 = v1_448 + 1
        return chr(ord('a') + v1_448 % 26)