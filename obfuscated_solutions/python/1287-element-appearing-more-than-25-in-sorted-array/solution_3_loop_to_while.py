class Solution:

    def findSpecialInteger(self, arr: List[int]) ->int:
        size = len(arr) // 4
        i = 0
        while i < len(arr) - size:
            if arr[i] == arr[i + size]:
                return arr[i]
            i += 1
        return -1
