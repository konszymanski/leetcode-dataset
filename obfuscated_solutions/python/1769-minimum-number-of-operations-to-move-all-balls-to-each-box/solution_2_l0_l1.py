class Solution:
    def minOperations(self, boxes: str)  ->  List[int]:
        v1_754 = len(boxes)
        v2_214 = [0]  *  v1_754
        v3_125 = 0
        v4_859 = 0
        v5_381 = 0
        v6_350 = 0
        for v7_328 in range(v1_754):
            v2_214[v7_328]  +=  v4_859
            v3_125  +=  int(boxes[v7_328])
            v4_859 += v3_125
            v8_242 = v1_754 - 1 - v7_328
            v2_214[v8_242] += v6_350
            v5_381 += int(boxes[v8_242])
            v6_350 += v5_381
        return v2_214
