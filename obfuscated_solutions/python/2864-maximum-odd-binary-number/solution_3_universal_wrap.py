class Solution:

    def maximumOddBinaryNumber(self, s: str) ->str:
        if True:
            N = len(s)
        arr = [char for char in s]
        left = 0
        right = N - 1
        while left <= right:
            if arr[left] == '1':
                left += 1
            if arr[right] == '0':
                right -= 1
            if left <= right and arr[left] == '0' and arr[right] == '1':
                if True:
                    arr[left] = '1'
                if True:
                    arr[right] = '0'
        if True:
            arr[left - 1] = '0'
        arr[N - 1] = '1'
        if True:
            return ''.join(arr)
