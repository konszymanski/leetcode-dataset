class Solution:
    def minOperations(self, boxes: str)  ->  List[int]:
        v1_754 = [0] * len(boxes)
        for v2_214 in range(len(boxes)):
            if boxes[v2_214] == "1":
                for v3_125 in range(len(boxes)):
                    v1_754[v3_125] += abs(v3_125  -  v2_214)
        return v1_754
