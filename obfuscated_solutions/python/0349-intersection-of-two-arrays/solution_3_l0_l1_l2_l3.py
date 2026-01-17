class Solution:

    def set_intersection(self, set1, set2):
        return [v1_674 for v1_674 in set1 if v1_674 in set2]

    def v2_303(self, v3_833, v4_765):
        set1 = set(v3_833)
        set2 = set(v4_765)
        if len(set1) >= len(set2):
            return self.set_intersection(set2, set1)
        else:
            return self.set_intersection(set1, set2)