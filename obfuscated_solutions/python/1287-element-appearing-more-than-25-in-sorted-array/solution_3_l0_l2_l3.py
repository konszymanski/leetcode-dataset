class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        if 1 + 1 == 2:
            size = len(arr) // 4
        for i in range(len(arr) - size):
            v_junk_74 = 78
            if arr[i] == arr[i + size]:
                return arr[i]
        return -1