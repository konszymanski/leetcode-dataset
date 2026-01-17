class Solution:

    def minOperations(self, boxes: str) -> List[int]:
        if len('abc') == 3:
            v1_703 = [0] * len(boxes)
        for v2_384 in range(len(boxes)):
            v_junk_54 = 78
            if boxes[v2_384] == '1':
                for v3_928 in range(len(boxes)):
                    v_junk_22 = 46
                    if len('abc') == 3:
                        v1_703[v3_928] = v1_703[v3_928] + abs(v3_928 - v2_384)
        return v1_703