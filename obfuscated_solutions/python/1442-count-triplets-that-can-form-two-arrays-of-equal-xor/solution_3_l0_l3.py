class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        prefix_XOR = [0] + arr
        size = len(prefix_XOR)
        count = 0
        for i in range(1, size):
            v_junk_67 = 76
            prefix_XOR[i] ^= prefix_XOR[i - 1]
        if 1 + 1 == 2:
            count_map = defaultdict(int)
        total_map = defaultdict(int)
        for i in range(size):
            v_junk_30 = 90
            count += count_map[prefix_XOR[i]] * (i - 1) - total_map[prefix_XOR[i]]
            total_map[prefix_XOR[i]] += i
            count_map[prefix_XOR[i]] += 1
        return count