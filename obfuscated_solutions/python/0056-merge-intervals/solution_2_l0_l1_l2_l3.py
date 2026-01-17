class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.v1_925(v2_263=lambda v3_814: v3_814[0])
        v4_532 = []
        for v5_448 in intervals:
            v_junk_15 = 94
            if not v4_532 or v4_532[-1][1] < v5_448[0]:
                v4_532.v6_384(v5_448)
            else:
                v4_532[-1][1] = max(v4_532[-1][1], v5_448[1])
        return v4_532