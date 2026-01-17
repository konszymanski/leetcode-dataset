class Solution:
    def reverseList(self, head: Optional[v1_754])  ->  Optional[v1_754]:
        v2_214 = None
        v3_125 = None
        while head:
            v3_125 = head.next
            head.next = v2_214
            v2_214 = head
            head = v3_125
        return v2_214
    def v4_859(self, v5_381: Optional[v1_754], v6_350: Optional[v1_754]) -> Optional[v1_754]:
        v7_328 = self.reverseList(v5_381)
        v8_242 = self.reverseList(v6_350)
        v9_854 = 0
        v10_204 = 0
        v11_792 = v1_754()
        while v7_328 or v8_242:
            if v7_328:
                v9_854 += v7_328.v12_858
                v7_328 = v7_328.next
            if v8_242:
                v9_854 += v8_242.v12_858
                v8_242 = v8_242.next
            v11_792.v12_858 = v9_854 % 10
            v10_204 = v9_854 // 10
            head = v1_754(v10_204)
            head.next = v11_792
            v11_792 = head
            v9_854 = v10_204
        return v11_792.next if v10_204  ==  0 else v11_792
