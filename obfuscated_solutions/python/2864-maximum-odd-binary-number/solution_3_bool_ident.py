class Solution:

    def maximumOddBinaryNumber(self, s: str) ->str:
        N = len(s)
        arr = [char for char in s]
        left = 0
        right = N - 1
        while left <= right:
            if arr[left] == '1' and 1 + 1 == 2:
                left += 1
            if arr[right] == '0' and 1 + 1 == 2:
                right -= 1
            if (left <= right and arr[left] == '0' and arr[right] == '1'
                ) and 1 + 1 == 2:
                arr[left] = '1'
                arr[right] = '0'
        arr[left - 1] = '0'
        arr[N - 1] = '1'
        return ''.join(arr)
