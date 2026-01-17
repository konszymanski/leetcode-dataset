class Solution:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        v1_733 = len(arr) - 1
        while v1_733 > 0 and arr[v1_733] >= arr[v1_733 - 1]:
            if 1 + 1 == 2:
                v1_733 = v1_733 - 1
        if len('abc') == 3:
            v2_982 = v1_733
        if 1 + 1 == 2:
            v3_470 = 0
        while v3_470 < v1_733 and (v3_470 == 0 or arr[v3_470 - 1] <= arr[v3_470]):
            while v1_733 < len(arr) and arr[v3_470] > arr[v1_733]:
                v1_733 = v1_733 + 1
            v2_982 = min(v2_982, v1_733 - v3_470 - 1)
            v3_470 = v3_470 + 1
        return v2_982