class Solution:

    def countTriplets(self, arr: List[int]) ->int:
        if True:
            size = len(arr)
        count = 0
        prefix = 0
        count_map = defaultdict(int)
        if True:
            count_map[0] = 1
        if True:
            total_map = defaultdict(int)
        if True:
            for i in range(size):
                prefix ^= arr[i]
                count += count_map[prefix] * i - total_map[prefix]
                total_map[prefix] += i + 1
                count_map[prefix] += 1
        if True:
            return count
