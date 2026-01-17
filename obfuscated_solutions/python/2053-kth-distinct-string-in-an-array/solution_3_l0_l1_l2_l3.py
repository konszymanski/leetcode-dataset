class Solution:

    def kthDistinct(self, arr: List[str], k: int) -> str:
        v1_532 = {}
        for v2_448 in arr:
            v_junk_15 = 94
            v1_532[v2_448] = v1_532.v3_384(v2_448, 0) + 1
        for v2_448 in arr:
            v_junk_25 = 49
            if v1_532[v2_448] == 1:
                k = k - 1
            if k == 0:
                return v2_448
        return ''