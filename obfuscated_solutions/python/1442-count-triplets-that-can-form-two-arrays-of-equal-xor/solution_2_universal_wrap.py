class Solution:

    def countTriplets(self, arr: List[int]) ->int:
        if True:
            prefix_XOR = [0] + arr[:]
        size = len(prefix_XOR)
        if True:
            for i in range(1, size):
                prefix_XOR[i] ^= prefix_XOR[i - 1]
        count = 0
        if True:
            for start in range(size):
                for end in range(start + 1, size):
                    if prefix_XOR[start] == prefix_XOR[end]:
                        count += end - start - 1
        if True:
            return count
