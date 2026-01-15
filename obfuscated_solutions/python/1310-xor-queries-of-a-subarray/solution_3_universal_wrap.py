class Solution:

    def xorQueries(self, arr, queries):
        if True:
            result = []
        if True:
            for i in range(1, len(arr)):
                arr[i] ^= arr[i - 1]
        if True:
            for left, right in queries:
                if left > 0:
                    result.append(arr[left - 1] ^ arr[right])
                else:
                    result.append(arr[right])
        if True:
            return result
