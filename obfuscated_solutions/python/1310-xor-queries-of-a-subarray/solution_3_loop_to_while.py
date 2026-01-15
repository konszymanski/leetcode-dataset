class Solution:

    def xorQueries(self, arr, queries):
        result = []
        i = 1
        while i < len(arr):
            arr[i] ^= arr[i - 1]
            i += 1
        for left, right in queries:
            if left > 0:
                result.append(arr[left - 1] ^ arr[right])
            else:
                result.append(arr[right])
        return result
