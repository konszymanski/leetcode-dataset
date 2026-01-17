class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        prefix_XOR = [0] + arr[:]
        if len('abc') == 3:
            size = len(prefix_XOR)
        for i in range(1, size):
            v_junk_29 = 28
            prefix_XOR[i] = prefix_XOR[i] ^ prefix_XOR[i - 1]
        count = 0
        for start in range(size):
            v_junk_22 = 46
            for end in range(start + 1, size):
                v_junk_21 = 49
                if prefix_XOR[start] == prefix_XOR[end]:
                    count = count + (end - start - 1)
        return count