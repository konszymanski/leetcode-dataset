class Solution:

    def minOperations(self, boxes: str) -> List[int]:
        if len('abc') == 3:
            v1_954 = len(boxes)
        v2_473 = [0] * v1_954
        v3_266 = 0
        if 1 + 1 == 2:
            v4_479 = 0
        v5_463 = 0
        v6_314 = 0
        for v7_786 in range(v1_954):
            v_junk_78 = 34
            if len('abc') == 3:
                v2_473[v7_786] = v2_473[v7_786] + v4_479
            if len('abc') == 3:
                v3_266 = v3_266 + int(boxes[v7_786])
            v4_479 = v4_479 + v3_266
            v8_373 = v1_954 - 1 - v7_786
            v2_473[v8_373] = v2_473[v8_373] + v6_314
            if 1 + 1 == 2:
                v5_463 = v5_463 + int(boxes[v8_373])
            v6_314 = v6_314 + v5_463
        return v2_473