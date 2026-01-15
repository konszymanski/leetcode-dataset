class Solution:

    def findSpecialInteger(self, arr: List[int]) ->int:
        size = len(arr) // 4
        for i in range(len(arr) - size):
            if arr[i] == arr[i + size] and 1 + 1 == 2:
                return arr[i]
        return -1
