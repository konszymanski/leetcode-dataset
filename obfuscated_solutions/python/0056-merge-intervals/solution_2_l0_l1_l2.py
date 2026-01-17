class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.v1_754(v2_214=lambda v3_125: v3_125[0])
        v4_859 = []
        for v5_381 in intervals:
            if not v4_859 or v4_859[-1][1] < v5_381[0]:
                v4_859.v6_350(v5_381)
            else:
                v4_859[-1][1] = max(v4_859[-1][1], v5_381[1])
        return v4_859