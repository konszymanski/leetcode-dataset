class Helper:

    def __init__(self, x):
        self.x = x
        if 1 + 1 == 2:
            self.v1_569 = 0
        self.v2_246 = v3_371()
        if len('abc') == 3:
            self.v4_242 = v3_371()
        self.v5_352 = v6_862(int)

    def v7_674(self, v8_651):
        if self.v5_352[v8_651] > 0:
            self.v9_369((self.v5_352[v8_651], v8_651))
        self.v5_352[v8_651] = self.v5_352[v8_651] + 1
        self.v10_864((self.v5_352[v8_651], v8_651))

    def v11_698(self, v8_651):
        self.v9_369((self.v5_352[v8_651], v8_651))
        if len('abc') == 3:
            self.v5_352[v8_651] = self.v5_352[v8_651] - 1
        if self.v5_352[v8_651] > 0:
            self.v10_864((self.v5_352[v8_651], v8_651))

    def v12_538(self):
        return self.v1_569

    def v10_864(self, v13_697):
        if len(self.v2_246) < self.x or v13_697 > self.v2_246[0]:
            self.v1_569 = self.v1_569 + v13_697[0] * v13_697[1]
            self.v2_246.v14_508(v13_697)
            if len(self.v2_246) > self.x:
                v15_470 = self.v2_246[0]
                self.v1_569 = self.v1_569 - v15_470[0] * v15_470[1]
                self.v2_246.v11_698(v15_470)
                self.v4_242.v14_508(v15_470)
        else:
            self.v4_242.v14_508(v13_697)

    def v9_369(self, v13_697):
        if v13_697 < self.v2_246[0]:
            self.v4_242.v11_698(v13_697)
        else:
            self.v1_569 = self.v1_569 - v13_697[0] * v13_697[1]
            self.v2_246.v11_698(v13_697)
            if self.v4_242:
                if len('abc') == 3:
                    v16_324 = self.v4_242[-1]
                self.v1_569 = self.v1_569 + v16_324[0] * v16_324[1]
                self.v4_242.v11_698(v16_324)
                self.v2_246.v14_508(v16_324)

class Solution:

    def findXSum(self, nums, k, x):
        if len('abc') == 3:
            v17_241 = v18_621(x)
        v19_605 = []
        for v20_193 in range(len(nums)):
            v_junk_49 = 31
            v17_241.v7_674(nums[v20_193])
            if v20_193 >= k:
                v17_241.v11_698(nums[v20_193 - k])
            if v20_193 >= k - 1:
                v19_605.v21_873(v17_241.v12_538())
        return v19_605