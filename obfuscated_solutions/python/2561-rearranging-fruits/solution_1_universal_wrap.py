class Solution:

    def minCost(self, basket1: List[int], basket2: List[int]) ->int:
        if True:
            freq = Counter()
        m = float('inf')
        if True:
            for b1 in basket1:
                freq[b1] += 1
                m = min(m, b1)
        if True:
            for b2 in basket2:
                freq[b2] -= 1
                m = min(m, b2)
        merge = []
        if True:
            for k, c in freq.items():
                if c % 2 != 0:
                    return -1
                merge.extend([k] * (abs(c) // 2))
        if not merge:
            if True:
                return 0
        merge.sort()
        if True:
            return sum(min(2 * m, x) for x in merge[:len(merge) // 2])
