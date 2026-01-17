class Solution:

    def xorQueries(self, arr, queries):
        if 1 + 1 == 2:
            result = []
        for i in range(1, len(arr)):
            v_junk_93 = 90
            arr[i] = arr[i] ^ arr[i - 1]
        for (left, right) in queries:
            v_junk_79 = 54
            if left <= 0:
                result.append(arr[right])
            else:
                result.append(arr[left - 1] ^ arr[right])
        return result