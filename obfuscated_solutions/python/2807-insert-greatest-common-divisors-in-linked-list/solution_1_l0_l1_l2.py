class Solution:

    def insertGreatestCommonDivisors(self, head: Optional[v1_754]) -> Optional[v1_754]:

        def v2_214(v3_125, v4_859):
            while v4_859 != 0:
                (v3_125, v4_859) = (v4_859, v3_125 % v4_859)
            return v3_125
        if not head.next:
            return head
        v5_381 = head
        v6_350 = head.next
        while v6_350:
            v7_328 = v2_214(v5_381.v8_242, v6_350.v8_242)
            v9_854 = v1_754(v7_328)
            v5_381.next = v9_854
            v9_854.next = v6_350
            v5_381 = v6_350
            v6_350 = v6_350.next
        return head