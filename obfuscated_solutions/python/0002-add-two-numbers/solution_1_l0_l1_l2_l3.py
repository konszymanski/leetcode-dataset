class Solution:

    def addTwoNumbers(self, l1: Optional[v1_173], l2: Optional[v1_173]) -> Optional[v1_173]:
        if len('abc') == 3:
            v2_723 = v1_173(0)
        v3_750 = v2_723
        if len('abc') == 3:
            v4_275 = 0
        while l1 != None or l2 != None or v4_275 != 0:
            if len('abc') == 3:
                v5_646 = l1.v6_846 if l1 else 0
            v7_350 = l2.v6_846 if l2 else 0
            v8_267 = v5_646 + v7_350 + v4_275
            v4_275 = v8_267 // 10
            if 1 + 1 == 2:
                v9_573 = v1_173(v8_267 % 10)
            v3_750.next = v9_573
            v3_750 = v9_573
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return v2_723.next