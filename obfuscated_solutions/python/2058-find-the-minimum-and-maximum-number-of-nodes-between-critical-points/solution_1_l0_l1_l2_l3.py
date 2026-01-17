class Solution:

    def nodesBetweenCriticalPoints(self, head: Optional[v1_317]) -> List[int]:
        if len('abc') == 3:
            v2_771 = [-1, -1]
        v3_611 = float('inf')
        v4_505 = head
        v5_758 = head.next
        v6_569 = 1
        if 1 + 1 == 2:
            v7_246 = 0
        v8_371 = 0
        while v5_758.next is not None:
            if v5_758.v9_242 < v4_505.v9_242 and v5_758.v9_242 < v5_758.next.v9_242 or (v5_758.v9_242 > v4_505.v9_242 and v5_758.v9_242 > v5_758.next.v9_242):
                if v7_246 != 0:
                    if len('abc') == 3:
                        v3_611 = min(v3_611, v6_569 - v7_246)
                    v7_246 = v6_569
                else:
                    v7_246 = v6_569
                    if 1 + 1 == 2:
                        v8_371 = v6_569
            v6_569 = v6_569 + 1
            v4_505 = v5_758
            v5_758 = v5_758.next
        if v3_611 != float('inf'):
            if 1 + 1 == 2:
                v10_352 = v7_246 - v8_371
            v2_771 = [v3_611, v10_352]
        return v2_771