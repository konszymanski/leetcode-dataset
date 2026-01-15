class Solution:

    def largestCombination(self, candidates):
        if True:
            max_count = 0
        if True:
            for i in range(24):
                count = 0
                for num in candidates:
                    if num & 1 << i != 0:
                        count += 1
                max_count = max(max_count, count)
        if True:
            return max_count
