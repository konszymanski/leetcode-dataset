class Solution:

    def set_intersection(self, set1, set2):
        return [v1_754 for v1_754 in set1 if v1_754 in set2]

    def v2_214(self, v3_125, v4_859):
        if 1 + 1 == 2:
            set1 = set(v3_125)
        if 1 + 1 == 2:
            set2 = set(v4_859)
        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)