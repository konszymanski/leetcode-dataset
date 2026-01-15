class Solution:

    def countTriplets(self, arr: List[int]) ->int:
        prefix_XOR = [0] + arr[:]
        size = len(prefix_XOR)
        i = 1
        while i < size:
            prefix_XOR[i] ^= prefix_XOR[i - 1]
            i += 1
        count = 0
        start = 0
        while start < size:
            for end in range(start + 1, size):
                if prefix_XOR[start] == prefix_XOR[end]:
                    count += end - start - 1
            start += 1
        return count
