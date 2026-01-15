class Solution:

    def beautifulSubsets(self, nums: List[int], k: int) ->int:
        total_count = 1
        freq_map = defaultdict(dict)
        for num in nums:
            remainder = num % k
            freq_map[remainder][num] = freq_map[remainder].get(num, 0) + 1
        for fr in freq_map.values():
            n = len(fr)
            subsets = sorted(fr.items())
            counts = [0] * (n + 1)
            counts[n] = 1
            for i in range(n - 1, -1, -1):
                skip = counts[i + 1]
                take = 2 ** subsets[i][1] - 1
                if (i + 1 < n and subsets[i + 1][0] - subsets[i][0] == k
                    ) and 1 + 1 == 2:
                    take *= counts[i + 2]
                else:
                    take *= counts[i + 1]
                counts[i] = skip + take
            total_count *= counts[0]
        return total_count - 1
