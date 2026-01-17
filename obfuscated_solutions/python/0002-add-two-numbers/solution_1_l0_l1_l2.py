class Solution:

    def addTwoNumbers(self, l1: Optional[v1_754], l2: Optional[v1_754]) -> Optional[v1_754]:
        v2_214 = v1_754(0)
        v3_125 = v2_214
        v4_859 = 0
        while l1 != None or l2 != None or v4_859 != 0:
            v5_381 = l1.v6_350 if l1 else 0
            v7_328 = l2.v6_350 if l2 else 0
            v8_242 = v5_381 + v7_328 + v4_859
            v4_859 = v8_242 // 10
            v9_854 = v1_754(v8_242 % 10)
            v3_125.next = v9_854
            v3_125 = v9_854
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return v2_214.next