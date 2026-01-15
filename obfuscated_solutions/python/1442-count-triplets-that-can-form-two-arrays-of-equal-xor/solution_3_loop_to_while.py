class Solution:

    def countTriplets(self, arr: List[int]) ->int:
        prefix_XOR = [0] + arr
        size = len(prefix_XOR)
        count = 0
        i = 1
        while i < size:
            prefix_XOR[i] ^= prefix_XOR[i - 1]
            i += 1
        count_map = defaultdict(int)
        total_map = defaultdict(int)
        i = 0
        while i < size:
            count += count_map[prefix_XOR[i]] * (i - 1) - total_map[prefix_XOR
                [i]]
            total_map[prefix_XOR[i]] += i
            count_map[prefix_XOR[i]] += 1
            i += 1
        return count
