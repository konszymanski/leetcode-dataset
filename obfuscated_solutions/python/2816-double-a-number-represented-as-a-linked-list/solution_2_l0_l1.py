class Solution:
    def doubleIt(self, head: Optional[v1_754]) -> Optional[v1_754]:
        v2_214 = []
        v3_125 = 0
        while head is not None:
            v2_214.v4_859(head.v3_125)
            head = head.next
        v5_381 = None
        while v2_214 or v3_125  !=  0:
            v5_381 = v1_754(0, v5_381)
            if v2_214:
                v3_125  +=  v2_214.v6_350() * 2
            v5_381.v3_125 = v3_125 % 10
            v3_125  //=  10
        return v5_381
