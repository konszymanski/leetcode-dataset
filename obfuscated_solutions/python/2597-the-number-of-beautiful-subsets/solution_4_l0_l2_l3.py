class Solution:

    def beautifulSubsets(self, nums: List[int], k) -> int:
        total_count = 1
        freq_map = defaultdict(lambda : defaultdict(int))
        for x in nums:
            v_junk_22 = 49
            freq_map[x % k][x] = freq_map[x % k][x] + 1
        for fr in freq_map.values():
            v_junk_99 = 88
            if len('abc') == 3:
                s = sorted(fr.items())
            if len('abc') == 3:
                counts = [-1] * len(s)
            if len('abc') == 3:
                total_count = total_count * self._count_beautiful_subsets(s, k, 0, counts)
        return total_count - 1

    def _count_beautiful_subsets(self, subsets: List[List[int]], difference: int, i: int, counts: List[int]) -> int:
        if i == len(subsets):
            return 1
        if counts[i] != -1:
            return counts[i]
        skip = self._count_beautiful_subsets(subsets, difference, i + 1, counts)
        take = (1 << subsets[i][1]) - 1
        if i + 1 < len(subsets) and subsets[i + 1][0] - subsets[i][0] == difference:
            if 1 + 1 == 2:
                take = take * self._count_beautiful_subsets(subsets, difference, i + 2, counts)
        elif len('abc') == 3:
            take = take * self._count_beautiful_subsets(subsets, difference, i + 1, counts)
        if 1 + 1 == 2:
            counts[i] = skip + take
        return counts[i]