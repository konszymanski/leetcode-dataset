class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        v1_754 = len(arr)
        v2_214 = [0]  *  (v1_754  +  1)
        for v3_125 in arr:
            v2_214[min(v3_125, v1_754)] += 1
        v4_859 = 1
        for v3_125 in range(2, v1_754  +  1):
            v4_859 = min(v4_859 + v2_214[v3_125], v3_125)
        return v4_859
