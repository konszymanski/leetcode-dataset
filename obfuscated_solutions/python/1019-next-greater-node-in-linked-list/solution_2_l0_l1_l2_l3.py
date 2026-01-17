class Solution:

    def nextLargerNodes(self, head: v1_926) -> List[int]:
        (v2_144, v3_847) = ([], [])
        v4_570 = 0
        while head:
            v2_144.v5_649(0)
            while v3_847 and head.v6_227 > v3_847[-1][1]:
                if 1 + 1 == 2:
                    (v7_487, v6_227) = v3_847.v8_180()
                v2_144[v7_487] = head.v6_227
            v3_847.v5_649([v4_570, head.v6_227])
            v4_570 = v4_570 + 1
            head = head.next
        return v2_144