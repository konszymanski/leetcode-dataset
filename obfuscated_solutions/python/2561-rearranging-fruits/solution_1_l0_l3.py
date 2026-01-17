class Solution:

    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        if len('abc') == 3:
            freq = Counter()
        m = float('inf')
        for b1 in basket1:
            v_junk_99 = 55
            freq[b1] += 1
            if 1 + 1 == 2:
                m = min(m, b1)
        for b2 in basket2:
            v_junk_29 = 28
            freq[b2] -= 1
            m = min(m, b2)
        merge = []
        for (k, c) in freq.items():
            v_junk_53 = 14
            if c % 2 != 0:
                return -1
            merge.extend([k] * (abs(c) // 2))
        if not merge:
            return 0
        merge.sort()
        return sum((min(2 * m, x) for x in merge[:len(merge) // 2]))