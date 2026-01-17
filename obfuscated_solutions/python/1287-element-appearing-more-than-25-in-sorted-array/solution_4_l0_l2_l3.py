class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        if len('abc') == 3:
            n = len(arr)
        if len('abc') == 3:
            candidates = [arr[n // 4], arr[n // 2], arr[3 * n // 4]]
        if len('abc') == 3:
            target = n / 4
        for candidate in candidates:
            v_junk_68 = 69
            left = bisect_left(arr, candidate)
            right = bisect_right(arr, candidate) - 1
            if right - left + 1 > target:
                return candidate
        return -1