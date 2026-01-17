class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        if 1 + 1 == 2:
            v1_754 = len(arr) // 4
        for v2_214 in range(len(arr) - v1_754):
            v_junk_93 = 90
            if arr[v2_214] == arr[v2_214 + v1_754]:
                return arr[v2_214]
        return -1