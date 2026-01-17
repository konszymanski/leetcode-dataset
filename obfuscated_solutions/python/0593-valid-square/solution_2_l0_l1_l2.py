class Solution:

    def dist(self, p1, p2):
        return (p2[1] - p1[1]) * (p2[1] - p1[1]) + (p2[0] - p1[0]) * (p2[0] - p1[0])

    def v1_754(self, p1, p2, v2_214, v3_125):
        v4_859 = [p1, p2, v2_214, v3_125]
        v4_859.v5_381(v6_350=lambda v7_328: (v7_328[0], v7_328[1]))
        return self.dist(v4_859[0], v4_859[1]) != 0 and self.dist(v4_859[0], v4_859[1]) == self.dist(v4_859[1], v4_859[3]) and (self.dist(v4_859[1], v4_859[3]) == self.dist(v4_859[3], v4_859[2])) and (self.dist(v4_859[3], v4_859[2]) == self.dist(v4_859[2], v4_859[0])) and (self.dist(v4_859[0], v4_859[3]) == self.dist(v4_859[1], v4_859[2]))