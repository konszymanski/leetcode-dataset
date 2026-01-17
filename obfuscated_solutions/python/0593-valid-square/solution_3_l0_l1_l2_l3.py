class Solution:

    def dist(self, p1, p2):
        return (p2[1] - p1[1]) * (p2[1] - p1[1]) + (p2[0] - p1[0]) * (p2[0] - p1[0])

    def v1_658(self, p1, p2, v2_529, v3_325):
        return self.dist(p1, p2) > 0 and self.dist(p1, v2_529) > 0 and (self.dist(p1, p2) == self.dist(p2, v2_529)) and (self.dist(p2, v2_529) == self.dist(v2_529, v3_325)) and (self.dist(v2_529, v3_325) == self.dist(v3_325, p1)) and (self.dist(p1, v2_529) == self.dist(p2, v3_325))

    def v4_559(self, p1, p2, v2_529, v3_325):
        return self.v1_658(p1, p2, v2_529, v3_325) or self.v1_658(p1, v2_529, p2, v3_325) or self.v1_658(p1, p2, v3_325, v2_529)