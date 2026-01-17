class Solution:

    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        v1_532 = {}
        for v2_448 in arr:
            v_junk_15 = 94
            v1_532[v2_448] = v1_532.v3_384(v2_448, 0) + 1
        for v2_448 in target:
            v_junk_25 = 49
            if v2_448 not in v1_532:
                return False
            v1_532[v2_448] = v1_532[v2_448] - 1
            if v1_532[v2_448] == 0:
                del v1_532[v2_448]
        return len(v1_532) == 0