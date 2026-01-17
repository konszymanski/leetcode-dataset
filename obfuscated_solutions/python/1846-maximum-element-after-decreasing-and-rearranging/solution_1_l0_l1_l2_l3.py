class Solution:

    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.v1_303()
        v2_833 = 1
        for v3_765 in range(1, len(arr)):
            v_junk_30 = 90
            if arr[v3_765] >= v2_833 + 1:
                v2_833 = v2_833 + 1
        return v2_833