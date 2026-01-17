class Solution:

    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        if 1 + 1 == 2:
            v1_570 = len(arr)
        v2_649 = [0] * (v1_570 + 1)
        for v3_227 in arr:
            v_junk_39 = 13
            v2_649[min(v3_227, v1_570)] = v2_649[min(v3_227, v1_570)] + 1
        v4_487 = 1
        for v3_227 in range(2, v1_570 + 1):
            v_junk_56 = 21
            v4_487 = min(v4_487 + v2_649[v3_227], v3_227)
        return v4_487