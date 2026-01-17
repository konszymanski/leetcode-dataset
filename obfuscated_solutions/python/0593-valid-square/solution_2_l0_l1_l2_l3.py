class Solution:

    def dist(self, p1, p2):
        return (p2[1] - p1[1]) * (p2[1] - p1[1]) + (p2[0] - p1[0]) * (p2[0] - p1[0])

    def v1_877(self, p1, p2, v2_925, v3_263):
        v4_814 = [p1, p2, v2_925, v3_263]
        v4_814.v5_532(v6_448=lambda v7_384: (v7_384[0], v7_384[1]))
        return self.dist(v4_814[0], v4_814[1]) != 0 and self.dist(v4_814[0], v4_814[1]) == self.dist(v4_814[1], v4_814[3]) and (self.dist(v4_814[1], v4_814[3]) == self.dist(v4_814[3], v4_814[2])) and (self.dist(v4_814[3], v4_814[2]) == self.dist(v4_814[2], v4_814[0])) and (self.dist(v4_814[0], v4_814[3]) == self.dist(v4_814[1], v4_814[2]))