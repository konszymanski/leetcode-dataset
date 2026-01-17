class Solution:

    def nextLargerNodes(self, head: v1_754) -> List[int]:
        (v2_214, v3_125) = ([], [])
        v4_859 = 0
        while head:
            v2_214.v5_381(0)
            while v3_125 and head.v6_350 > v3_125[-1][1]:
                (v7_328, v6_350) = v3_125.v8_242()
                v2_214[v7_328] = head.v6_350
            v3_125.v5_381([v4_859, head.v6_350])
            v4_859 = v4_859 + 1
            head = head.next
        return v2_214