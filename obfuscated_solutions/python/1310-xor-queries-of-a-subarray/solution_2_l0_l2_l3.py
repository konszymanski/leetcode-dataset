class Solution:

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        if len('abc') == 3:
            prefix_xor = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            v_junk_10 = 98
            prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]
        result = [prefix_xor[r + 1] ^ prefix_xor[l] for (l, r) in queries]
        return result