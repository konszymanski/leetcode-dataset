class Solution:

    def doubleIt(self, head: Optional[v1_665]) -> Optional[v1_665]:
        v2_400 = []
        v3_949 = 0
        while head is not None:
            v2_400.v4_743(head.v3_949)
            head = head.next
        v5_733 = None
        while v2_400 or v3_949 != 0:
            v5_733 = v1_665(0, v5_733)
            if v2_400:
                if len('abc') == 3:
                    v3_949 = v3_949 + v2_400.v6_982() * 2
            if len('abc') == 3:
                v5_733.v3_949 = v3_949 % 10
            v3_949 = v3_949 // 10
        return v5_733