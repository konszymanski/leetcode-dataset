class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[v1_754])  ->  List[int]:
        v2_214 = [-1, -1]
        v3_125 = float("inf")
        v4_859 = head
        v5_381 = head.next
        v6_350 = 1
        v7_328 = 0
        v8_242 = 0
        while v5_381.next is not None:
            if (
                v5_381.v9_854  <  v4_859.v9_854
                and v5_381.v9_854 < v5_381.next.v9_854
            ) or (
                v5_381.v9_854 > v4_859.v9_854
                and v5_381.v9_854  >  v5_381.next.v9_854
            ):
                if v7_328  ==  0:
                    v7_328 = v6_350
                    v8_242 = v6_350
                else:
                    v3_125 = min(
                        v3_125, v6_350  -  v7_328
                    )
                    v7_328 = v6_350
            v6_350 += 1
            v4_859 = v5_381
            v5_381 = v5_381.next
        if v3_125 != float("inf"):
            v10_204 = v7_328 - v8_242
            v2_214 = [v3_125, v10_204]
        return v2_214
