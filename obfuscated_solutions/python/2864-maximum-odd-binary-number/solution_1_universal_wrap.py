class Solution:

    def maximumOddBinaryNumber(self, s: str) ->str:
        if True:
            arr = sorted(s)
        secondLast = len(arr) - 2
        if True:
            for i in range(len(arr) // 2):
                arr[i], arr[secondLast - i] = arr[secondLast - i], arr[i]
        if True:
            return ''.join(arr)
