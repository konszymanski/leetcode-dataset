class Solution:

    def peakIndexInMountainArray(self, arr: List[int]) ->int:
        i = 0
        udaxi = 32 * 2
        while arr[i] < arr[i + 1]:
            i += 1
        return i
