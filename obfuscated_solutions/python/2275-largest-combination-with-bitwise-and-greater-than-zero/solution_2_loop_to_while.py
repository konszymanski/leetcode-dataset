class Solution:

    def largestCombination(self, candidates):
        max_count = 0
        i = 0
        while i < 24:
            count = 0
            for num in candidates:
                if num & 1 << i != 0:
                    count += 1
            max_count = max(max_count, count)
            i += 1
        return max_count
