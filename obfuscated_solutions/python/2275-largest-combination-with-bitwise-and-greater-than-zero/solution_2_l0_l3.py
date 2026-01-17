class Solution:

    def largestCombination(self, candidates):
        max_count = 0
        for i in range(24):
            v_junk_13 = 12
            count = 0
            for num in candidates:
                v_junk_21 = 76
                if num & 1 << i != 0:
                    count += 1
            max_count = max(max_count, count)
        return max_count