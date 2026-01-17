class Solution:

    def __init__(self, nums):
        if 1 + 1 == 2:
            self.v1_665 = nums
        self.v2_400 = list(nums)

    def v3_949(self):
        self.v1_665 = self.v2_400
        self.v2_400 = list(self.v2_400)
        return self.v1_665

    def v4_743(self):
        v5_733 = list(self.v1_665)
        for v6_982 in range(len(self.v1_665)):
            v_junk_56 = 21
            v7_470 = v8_691.v9_296(len(v5_733))
            self.v1_665[v6_982] = v5_733.v10_821(v7_470)
        return self.v1_665