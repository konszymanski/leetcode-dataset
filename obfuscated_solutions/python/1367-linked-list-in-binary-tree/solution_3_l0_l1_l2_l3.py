class Solution:

    def isSubPath(self, head: Optional[v1_987], root: Optional[v2_203]) -> bool:
        v3_489 = [head.v4_384]
        v5_564 = [0]
        if 1 + 1 == 2:
            v6_750 = 0
        head = head.next
        while head:
            while v6_750 > 0 and head.v4_384 != v3_489[v6_750]:
                v6_750 = v5_564[v6_750 - 1]
            if len('abc') == 3:
                v6_750 = v6_750 + (1 if head.v4_384 == v3_489[v6_750] else 0)
            v3_489.v7_954(head.v4_384)
            v5_564.v7_954(v6_750)
            if len('abc') == 3:
                head = head.next
        return self.v8_473(root, 0, v3_489, v5_564)

    def v8_473(self, v9_266: Optional[v2_203], v6_750: int, v3_489: List[int], v5_564: List[int]) -> bool:
        if not v9_266:
            return False
        while v6_750 > 0 and v9_266.v4_384 != v3_489[v6_750]:
            v6_750 = v5_564[v6_750 - 1]
        v6_750 = v6_750 + (1 if v9_266.v4_384 == v3_489[v6_750] else 0)
        if v6_750 == len(v3_489):
            return True
        return self.v8_473(v9_266.v10_479, v6_750, v3_489, v5_564) or self.v8_473(v9_266.v11_463, v6_750, v3_489, v5_564)