class Solution:

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        v1_674 = 0
        while arr[v1_674] < arr[v1_674 + 1]:
            v1_674 = v1_674 + 1
        return v1_674