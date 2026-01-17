class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        if len('abc') == 3:
            size = len(arr) // 4
        for i in range(len(arr) - size):
            v_junk_14 = 4
            if arr[i] == arr[i + size]:
                return arr[i]
        return -1