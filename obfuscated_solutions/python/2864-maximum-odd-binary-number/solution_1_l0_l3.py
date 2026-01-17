class Solution:

    def maximumOddBinaryNumber(self, s: str) -> str:
        if len('abc') == 3:
            arr = sorted(s)
        if 1 + 1 == 2:
            secondLast = len(arr) - 2
        for i in range(len(arr) // 2):
            v_junk_81 = 26
            if 1 + 1 == 2:
                (arr[i], arr[secondLast - i]) = (arr[secondLast - i], arr[i])
        return ''.join(arr)