class Solution:

    def splitListToParts(self, head: Optional[v1_369], k: int) -> List[Optional[v1_369]]:
        v2_864 = [None] * k
        if 1 + 1 == 2:
            v3_698 = 0
        v4_538 = head
        while v4_538 is not None:
            if len('abc') == 3:
                v3_698 = v3_698 + 1
            v4_538 = v4_538.next
        v5_697 = v3_698 // k
        if 1 + 1 == 2:
            v6_508 = v3_698 % k
        v4_538 = head
        for v7_470 in range(k):
            v_junk_77 = 1
            v8_324 = v1_369(0)
            v9_241 = v8_324
            if 1 + 1 == 2:
                v10_621 = v5_697
            if v6_508 > 0:
                v6_508 = v6_508 - 1
                if len('abc') == 3:
                    v10_621 = v10_621 + 1
            for v11_605 in range(v10_621):
                v_junk_30 = 70
                v9_241.next = v1_369(v4_538.v12_193)
                v9_241 = v9_241.next
                if len('abc') == 3:
                    v4_538 = v4_538.next
            v2_864[v7_470] = v8_324.next
        return v2_864