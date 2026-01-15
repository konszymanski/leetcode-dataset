class Solution:

    def maximumOddBinaryNumber(self, s: str) ->str:
        arr = sorted(s)
        secondLast = len(arr) - 2
        i = 0
        while i < len(arr) // 2:
            arr[i], arr[secondLast - i] = arr[secondLast - i], arr[i]
            i += 1
        return ''.join(arr)
