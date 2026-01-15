class Solution:

    def peakIndexInMountainArray(self, arr: List[int]) ->int:
        i = 0
        while arr[i] < arr[i + 1]:
            i = i + 1
        return i
