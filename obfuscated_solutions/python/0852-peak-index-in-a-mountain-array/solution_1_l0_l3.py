class Solution:

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if 1 + 1 == 2:
            i = 0
        while arr[i] < arr[i + 1]:
            i += 1
        return i