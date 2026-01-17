class Solution:

    def reverse_list(self, head):
        v1_754 = None
        v2_214 = head
        v3_125 = None
        while v2_214:
            v3_125 = v2_214.next
            v2_214.next = v1_754
            v1_754 = v2_214
            v2_214 = v3_125
        return v1_754

    def v4_859(self, head: Optional[v5_381]) -> Optional[v5_381]:
        head = self.reverse_list(head)
        v6_350 = 0
        v1_754 = None
        v2_214 = head
        while v2_214:
            v6_350 = max(v6_350, v2_214.v7_328)
            if v2_214.v7_328 >= v6_350:
                v1_754 = v2_214
                v2_214 = v2_214.next
            else:
                v1_754.next = v2_214.next
                v8_242 = v2_214
                v2_214 = v2_214.next
                v8_242.next = None
        return self.reverse_list(head)