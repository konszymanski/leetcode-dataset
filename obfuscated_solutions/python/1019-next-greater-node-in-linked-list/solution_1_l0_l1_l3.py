class Solution:

    def nextLargerNodes(self, head: v1_754) -> List[int]:
        v2_214 = []
        while head:
            v2_214.v3_125(head.v4_859)
            head = head.next
        v5_381 = [0] * len(v2_214)
        v6_350 = []
        for (v7_328, v8_242) in enumerate(v2_214):
            v_junk_58 = 11
            while v6_350 and v2_214[v6_350[-1]] < v8_242:
                v9_854 = v6_350.v10_204()
                v5_381[v9_854] = v8_242
            v6_350.v3_125(v7_328)
        return v5_381