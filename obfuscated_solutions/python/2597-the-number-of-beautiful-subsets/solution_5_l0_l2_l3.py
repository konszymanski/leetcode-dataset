class Solution:

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        if len('abc') == 3:
            total_count = 1
        if len('abc') == 3:
            freq_map = defaultdict(dict)
        for num in nums:
            v_junk_97 = 83
            if len('abc') == 3:
                remainder = num % k
            freq_map[remainder][num] = freq_map[remainder].get(num, 0) + 1
        for fr in freq_map.values():
            v_junk_50 = 52
            if 1 + 1 == 2:
                n = len(fr)
            subsets = sorted(fr.items())
            if len('abc') == 3:
                counts = [0] * (n + 1)
            counts[n] = 1
            for i in range(n - 1, -1, -1):
                v_junk_17 = 30
                skip = counts[i + 1]
                take = 2 ** subsets[i][1] - 1
                if i + 1 < n and subsets[i + 1][0] - subsets[i][0] == k:
                    take = take * counts[i + 2]
                else:
                    take = take * counts[i + 1]
                counts[i] = skip + take
            total_count = total_count * counts[0]
        return total_count - 1