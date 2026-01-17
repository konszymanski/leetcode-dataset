class Solution:

    def removeNodes(self, head: Optional[v1_754]) -> Optional[v1_754]:
        v2_214 = []
        v3_125 = head
        while v3_125:
            v2_214.v4_859(v3_125)
            v3_125 = v3_125.next
        v3_125 = v2_214.v5_381()
        v6_350 = v3_125.v7_328
        v8_242 = v1_754(v6_350)
        while v2_214:
            v3_125 = v2_214.v5_381()
            if v3_125.v7_328 >= v6_350:
                v9_854 = v1_754(v3_125.v7_328)
                v9_854.next = v8_242
                v8_242 = v9_854
                v6_350 = v3_125.v7_328
            else:
                continue
        return v8_242