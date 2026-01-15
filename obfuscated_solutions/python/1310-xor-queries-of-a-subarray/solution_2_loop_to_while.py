class Solution:

    def xorQueries(self, arr: List[int], queries: List[List[int]]) ->List[int]:
        prefix_xor = [0] * (len(arr) + 1)
        i = 0
        while i < len(arr):
            prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]
            i += 1
        result = [(prefix_xor[r + 1] ^ prefix_xor[l]) for l, r in queries]
        return result
