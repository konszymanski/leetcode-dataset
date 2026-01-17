class Solution:
    def splitListToParts(
        self, head: Optional[v1_754], k: int
    )  ->  List[Optional[v1_754]]:
        v2_214 = [None]  *  k
        v3_125 = 0
        v4_859 = head
        while v4_859 is not None:
            v3_125  +=  1
            v4_859 = v4_859.next
        v5_381 = v3_125  //  k
        v6_350 = v3_125  %  k
        v4_859 = head
        v7_328 = v4_859
        for v8_242 in range(k):
            v9_854 = v4_859
            v10_204 = v5_381
            if v6_350  >  0:
                v6_350 -= 1
                v10_204 += 1
            v11_792 = 0
            while v11_792  <  v10_204:
                v7_328 = v4_859
                if v4_859 is not None:
                    v4_859 = v4_859.next
                v11_792 += 1
            if v7_328 is not None:
                v7_328.next = None
            v2_214[v8_242] = v9_854
        return v2_214
