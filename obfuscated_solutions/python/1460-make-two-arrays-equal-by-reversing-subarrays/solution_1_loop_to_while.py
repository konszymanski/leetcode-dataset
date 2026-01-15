class Solution:

    def canBeEqual(self, target: List[int], arr: List[int]) ->bool:
        arr.sort()
        target.sort()
        i = 0
        while i < len(arr):
            if arr[i] != target[i]:
                return False
            i += 1
        return True
