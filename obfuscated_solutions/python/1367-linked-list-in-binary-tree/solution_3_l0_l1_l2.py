class Solution:

    def isSubPath(self, head: Optional[v1_754], root: Optional[v2_214]) -> bool:
        v3_125 = [head.v4_859]
        v5_381 = [0]
        v6_350 = 0
        head = head.next
        while head:
            while v6_350 > 0 and head.v4_859 != v3_125[v6_350]:
                v6_350 = v5_381[v6_350 - 1]
            v6_350 = v6_350 + (1 if head.v4_859 == v3_125[v6_350] else 0)
            v3_125.v7_328(head.v4_859)
            v5_381.v7_328(v6_350)
            head = head.next
        return self.v8_242(root, 0, v3_125, v5_381)

    def v8_242(self, v9_854: Optional[v2_214], v6_350: int, v3_125: List[int], v5_381: List[int]) -> bool:
        if not v9_854:
            return False
        while v6_350 > 0 and v9_854.v4_859 != v3_125[v6_350]:
            v6_350 = v5_381[v6_350 - 1]
        v6_350 = v6_350 + (1 if v9_854.v4_859 == v3_125[v6_350] else 0)
        if v6_350 == len(v3_125):
            return True
        return self.v8_242(v9_854.v10_204, v6_350, v3_125, v5_381) or self.v8_242(v9_854.v11_792, v6_350, v3_125, v5_381)