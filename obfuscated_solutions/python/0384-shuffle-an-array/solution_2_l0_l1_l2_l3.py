class Solution:

    def __init__(self, nums):
        if len('abc') == 3:
            self.v1_370 = nums
        self.v2_926 = list(nums)

    def v3_144(self):
        self.v1_370 = self.v2_926
        self.v2_926 = list(self.v2_926)
        return self.v1_370

    def v4_847(self):
        for v5_570 in range(len(self.v1_370)):
            v_junk_15 = 85
            v6_649 = v7_227.v8_487(v5_570, len(self.v1_370))
            (self.v1_370[v5_570], self.v1_370[v6_649]) = (self.v1_370[v6_649], self.v1_370[v5_570])
        return self.v1_370