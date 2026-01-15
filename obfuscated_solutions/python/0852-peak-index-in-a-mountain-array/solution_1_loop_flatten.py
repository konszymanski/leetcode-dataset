class Solution:

    def peakIndexInMountainArray(self, arr: List[int]) ->int:
        i = 0
        while True:
            if not arr[i] < arr[i + 1]:
                break
            i += 1
        return i
