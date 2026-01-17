class Solution:

    def xorQueries(self, arr, queries):
        result = []
        for i in range(1, len(arr)):
            v_junk_14 = 4
            arr[i] ^= arr[i - 1]
        for (left, right) in queries:
            v_junk_21 = 28
            if left > 0:
                result.append(arr[left - 1] ^ arr[right])
            else:
                result.append(arr[right])
        return result