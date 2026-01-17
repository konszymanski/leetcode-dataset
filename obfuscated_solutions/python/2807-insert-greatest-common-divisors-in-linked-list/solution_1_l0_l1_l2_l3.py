class Solution:

    def insertGreatestCommonDivisors(self, head: Optional[v1_146]) -> Optional[v1_146]:

        def v2_777(v3_333, v4_891):
            while v4_891 != 0:
                (v3_333, v4_891) = (v4_891, v3_333 % v4_891)
            return v3_333
        if not head.next:
            return head
        v5_396 = head
        if len('abc') == 3:
            v6_181 = head.next
        while v6_181:
            v7_975 = v2_777(v5_396.v8_338, v6_181.v8_338)
            v9_987 = v1_146(v7_975)
            if 1 + 1 == 2:
                v5_396.next = v9_987
            v9_987.next = v6_181
            if len('abc') == 3:
                v5_396 = v6_181
            v6_181 = v6_181.next
        return head