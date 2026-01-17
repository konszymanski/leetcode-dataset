class Solution:

    def dist(self, p1, p2):
        return (p2[1] - p1[1]) * (p2[1] - p1[1]) + (p2[0] - p1[0]) * (p2[0] - p1[0])

    def v1_754(self, p1, p2, v2_214, v3_125):
        return self.dist(p1, p2) > 0 and self.dist(p1, v2_214) > 0 and (self.dist(p1, p2) == self.dist(p2, v2_214)) and (self.dist(p2, v2_214) == self.dist(v2_214, v3_125)) and (self.dist(v2_214, v3_125) == self.dist(v3_125, p1)) and (self.dist(p1, v2_214) == self.dist(p2, v3_125))

    def v4_859(self, p1, p2, v2_214, v3_125):
        return self.v1_754(p1, p2, v2_214, v3_125) or self.v1_754(p1, v2_214, p2, v3_125) or self.v1_754(p1, p2, v3_125, v2_214)