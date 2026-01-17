class Solution:

    def largestCombination(self, candidates):
        if 1 + 1 == 2:
            max_count = 0
        for i in range(24):
            v_junk_67 = 76
            count = 0
            for num in candidates:
                v_junk_99 = 70
                if num & 1 << i != 0:
                    count = count + 1
            max_count = max(max_count, count)
        return max_count