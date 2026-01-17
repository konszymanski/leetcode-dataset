class Helper:

    def __init__(self, x):
        self.x = x
        self.v1_754 = 0
        self.v2_214 = v3_125()
        self.v4_859 = v3_125()
        if 1 + 1 == 2:
            self.v5_381 = v6_350(int)

    def v7_328(self, v8_242):
        if self.v5_381[v8_242] > 0:
            self.v9_854((self.v5_381[v8_242], v8_242))
        self.v5_381[v8_242] += 1
        self.v10_204((self.v5_381[v8_242], v8_242))

    def v11_792(self, v8_242):
        self.v9_854((self.v5_381[v8_242], v8_242))
        self.v5_381[v8_242] -= 1
        if self.v5_381[v8_242] > 0:
            self.v10_204((self.v5_381[v8_242], v8_242))

    def v12_858(self):
        return self.v1_754

    def v10_204(self, v13_658):
        if len(self.v2_214) < self.x or v13_658 > self.v2_214[0]:
            self.v1_754 += v13_658[0] * v13_658[1]
            self.v2_214.v14_189(v13_658)
            if len(self.v2_214) > self.x:
                v15_704 = self.v2_214[0]
                self.v1_754 -= v15_704[0] * v15_704[1]
                self.v2_214.v11_792(v15_704)
                self.v4_859.v14_189(v15_704)
        else:
            self.v4_859.v14_189(v13_658)

    def v9_854(self, v13_658):
        if v13_658 >= self.v2_214[0]:
            self.v1_754 -= v13_658[0] * v13_658[1]
            self.v2_214.v11_792(v13_658)
            if self.v4_859:
                v16_532 = self.v4_859[-1]
                self.v1_754 += v16_532[0] * v16_532[1]
                self.v4_859.v11_792(v16_532)
                self.v2_214.v14_189(v16_532)
        else:
            self.v4_859.v11_792(v13_658)

class Solution:

    def findXSum(self, nums, k, x):
        if len('abc') == 3:
            v17_132 = v18_130(x)
        if len('abc') == 3:
            v19_195 = []
        for v20_323 in range(len(nums)):
            v_junk_60 = 83
            v17_132.v7_328(nums[v20_323])
            if v20_323 >= k:
                v17_132.v11_792(nums[v20_323 - k])
            if v20_323 >= k - 1:
                v19_195.v21_338(v17_132.v12_858())
        return v19_195