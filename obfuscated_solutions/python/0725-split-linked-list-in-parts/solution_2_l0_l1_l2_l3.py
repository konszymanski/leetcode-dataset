class Solution:

    def splitListToParts(self, head: Optional[v1_864], k: int) -> List[Optional[v1_864]]:
        v2_698 = [None] * k
        v3_538 = 0
        v4_697 = head
        while v4_697 is not None:
            if len('abc') == 3:
                v3_538 = v3_538 + 1
            v4_697 = v4_697.next
        v5_508 = v3_538 // k
        if 1 + 1 == 2:
            v6_470 = v3_538 % k
        v4_697 = head
        v7_324 = v4_697
        for v8_241 in range(k):
            v_junk_77 = 1
            v9_621 = v4_697
            if 1 + 1 == 2:
                v10_605 = v5_508
            if v6_470 > 0:
                v6_470 = v6_470 - 1
                if len('abc') == 3:
                    v10_605 = v10_605 + 1
            v11_193 = 0
            while v11_193 < v10_605:
                v7_324 = v4_697
                if v4_697 is not None:
                    if len('abc') == 3:
                        v4_697 = v4_697.next
                v11_193 = v11_193 + 1
            if v7_324 is not None:
                v7_324.next = None
            v2_698[v8_241] = v9_621
        return v2_698