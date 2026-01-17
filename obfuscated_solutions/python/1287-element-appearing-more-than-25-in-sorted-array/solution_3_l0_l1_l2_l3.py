class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        v1_658 = len(arr) // 4
        for v2_529 in range(len(arr) - v1_658):
            v_junk_29 = 28
            if arr[v2_529] == arr[v2_529 + v1_658]:
                return arr[v2_529]
        return -1