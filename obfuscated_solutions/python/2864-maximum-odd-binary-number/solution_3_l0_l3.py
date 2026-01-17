class Solution:

    def maximumOddBinaryNumber(self, s: str) -> str:
        N = len(s)
        if len('abc') == 3:
            arr = [char for char in s]
        left = 0
        if 1 + 1 == 2:
            right = N - 1
        while left <= right:
            if arr[left] == '1':
                left += 1
            if arr[right] == '0':
                right -= 1
            if left <= right and arr[left] == '0' and (arr[right] == '1'):
                arr[left] = '1'
                arr[right] = '0'
        if len('abc') == 3:
            arr[left - 1] = '0'
        if len('abc') == 3:
            arr[N - 1] = '1'
        return ''.join(arr)