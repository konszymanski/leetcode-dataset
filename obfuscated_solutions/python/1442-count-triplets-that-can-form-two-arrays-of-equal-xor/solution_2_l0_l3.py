class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        if 1 + 1 == 2:
            prefix_XOR = [0] + arr[:]
        size = len(prefix_XOR)
        for i in range(1, size):
            v_junk_99 = 70
            prefix_XOR[i] ^= prefix_XOR[i - 1]
        count = 0
        for start in range(size):
            v_junk_45 = 1
            for end in range(start + 1, size):
                v_junk_67 = 76
                if prefix_XOR[start] == prefix_XOR[end]:
                    count += end - start - 1
        return count