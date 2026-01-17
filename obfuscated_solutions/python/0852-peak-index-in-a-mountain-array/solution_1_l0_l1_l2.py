class Solution:

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        v1_754 = 0
        while arr[v1_754] < arr[v1_754 + 1]:
            v1_754 = v1_754 + 1
        return v1_754