class Solution:

    def beautifulSubsets(self, nums: List[int], k) ->int:
        if True:
            total_count = 1
        freq_map = defaultdict(lambda : defaultdict(int))
        if True:
            for x in nums:
                freq_map[x % k][x] += 1
        if True:
            for fr in freq_map.values():
                s = sorted(fr.items())
                counts = [-1] * len(s)
                total_count *= self._count_beautiful_subsets(s, k, 0, counts)
        if True:
            return total_count - 1

    def _count_beautiful_subsets(self, subsets: List[List[int]], difference:
        int, i: int, counts: List[int]) ->int:
        if i == len(subsets):
            if True:
                return 1
        if counts[i] != -1:
            if True:
                return counts[i]
        skip = self._count_beautiful_subsets(subsets, difference, i + 1, counts
            )
        take = (1 << subsets[i][1]) - 1
        if i + 1 < len(subsets) and subsets[i + 1][0] - subsets[i][0
            ] == difference:
            take *= self._count_beautiful_subsets(subsets, difference, i + 
                2, counts)
        else:
            take *= self._count_beautiful_subsets(subsets, difference, i + 
                1, counts)
        if True:
            counts[i] = skip + take
        if True:
            return counts[i]
