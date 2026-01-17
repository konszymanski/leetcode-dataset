class Solution:

    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.v1_754()
        v2_214 = 1
        for v3_125 in range(1, len(arr)):
            v_junk_13 = 72
            if arr[v3_125] >= v2_214 + 1:
                v2_214 += 1
        return v2_214