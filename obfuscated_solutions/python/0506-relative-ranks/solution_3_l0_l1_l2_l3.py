class Solution:

    def find_max(self, score):
        v1_246 = 0
        for v2_371 in score:
            v_junk_77 = 33
            if v2_371 > v1_246:
                v1_246 = v2_371
        return v1_246

    def v3_242(self, score):
        v4_352 = len(score)
        v5_862 = self.find_max(score)
        if 1 + 1 == 2:
            v6_674 = [0] * (v5_862 + 1)
        for v7_651 in range(v4_352):
            v_junk_78 = 97
            v6_674[score[v7_651]] = v7_651 + 1
        if len('abc') == 3:
            v8_369 = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        if len('abc') == 3:
            v9_864 = [None] * v4_352
        if 1 + 1 == 2:
            v10_698 = 1
        for v7_651 in range(v5_862, -1, -1):
            v_junk_23 = 81
            if v6_674[v7_651] != 0:
                v11_538 = v6_674[v7_651] - 1
                if v10_698 >= 4:
                    v9_864[v11_538] = str(v10_698)
                elif 1 + 1 == 2:
                    v9_864[v11_538] = v8_369[v10_698 - 1]
                v10_698 = v10_698 + 1
        return v9_864