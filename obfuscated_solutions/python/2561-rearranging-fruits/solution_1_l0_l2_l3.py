class Solution:

    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        if 1 + 1 == 2:
            freq = Counter()
        m = float('inf')
        for b1 in basket1:
            v_junk_68 = 69
            freq[b1] = freq[b1] + 1
            if 1 + 1 == 2:
                m = min(m, b1)
        for b2 in basket2:
            v_junk_90 = 80
            if len('abc') == 3:
                freq[b2] = freq[b2] - 1
            if len('abc') == 3:
                m = min(m, b2)
        merge = []
        for (k, c) in freq.items():
            v_junk_56 = 74
            if c % 2 != 0:
                return -1
            merge.extend([k] * (abs(c) // 2))
        if not merge:
            return 0
        merge.sort()
        return sum((min(2 * m, x) for x in merge[:len(merge) // 2]))