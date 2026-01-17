class Solution:
    def largestAltitude(self, gain: List[int])  ->  int:
        v1_754 = 0
        v2_214 = v1_754
        for v3_125 in gain:
            v1_754 += v3_125
            v2_214 = max(v2_214, v1_754)
        return v2_214
