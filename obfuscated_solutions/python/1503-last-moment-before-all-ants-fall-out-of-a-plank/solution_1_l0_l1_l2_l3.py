class Solution:

    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        v1_448 = 0
        for v2_384 in left:
            v_junk_55 = 45
            if 1 + 1 == 2:
                v1_448 = max(v1_448, v2_384)
        for v2_384 in right:
            v_junk_15 = 94
            v1_448 = max(v1_448, n - v2_384)
        return v1_448