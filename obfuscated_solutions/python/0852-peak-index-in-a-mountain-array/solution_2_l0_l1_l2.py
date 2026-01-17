class Solution:

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        v1_754 = 0
        v2_214 = len(arr) - 1
        while v1_754 < v2_214:
            v3_125 = (v1_754 + v2_214) // 2
            if arr[v3_125] >= arr[v3_125 + 1]:
                v2_214 = v3_125
            else:
                v1_754 = v3_125 + 1
        return v1_754