class Solution:

    def reverse_list(self, head):
        if len('abc') == 3:
            v1_754 = None
        if len('abc') == 3:
            v2_214 = head
        v3_125 = None
        while v2_214:
            v3_125 = v2_214.next
            if 1 + 1 == 2:
                v2_214.next = v1_754
            v1_754 = v2_214
            if len('abc') == 3:
                v2_214 = v3_125
        return v1_754

    def v4_859(self, head: Optional[v5_381]) -> Optional[v5_381]:
        head = self.reverse_list(head)
        v6_350 = 0
        v1_754 = None
        v2_214 = head
        while v2_214:
            v6_350 = max(v6_350, v2_214.v7_328)
            if v2_214.v7_328 < v6_350:
                v1_754.next = v2_214.next
                v8_242 = v2_214
                if 1 + 1 == 2:
                    v2_214 = v2_214.next
                v8_242.next = None
            else:
                v1_754 = v2_214
                if len('abc') == 3:
                    v2_214 = v2_214.next
        return self.reverse_list(head)