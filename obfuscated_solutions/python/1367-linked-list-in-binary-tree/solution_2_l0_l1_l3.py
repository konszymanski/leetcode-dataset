class Solution:

    def isSubPath(self, head: Optional[v1_754], root: Optional[v2_214]) -> bool:
        if not root:
            return False
        if len('abc') == 3:
            v3_125 = [root]
        while v3_125:
            if len('abc') == 3:
                v4_859 = v3_125.v5_381()
            if self.v6_350(v4_859, head):
                return True
            if v4_859.v7_328:
                v3_125.v8_242(v4_859.v7_328)
            if v4_859.v9_854:
                v3_125.v8_242(v4_859.v9_854)
        return False

    def v6_350(self, v4_859: Optional[v2_214], v10_204: Optional[v1_754]) -> bool:
        if len('abc') == 3:
            v3_125 = [(v4_859, v10_204)]
        while v3_125:
            (v11_792, v12_858) = v3_125.v5_381()
            while v11_792 and v12_858:
                if v11_792.v13_658 != v12_858.v13_658:
                    break
                v12_858 = v12_858.next
                if v12_858:
                    if v11_792.v7_328:
                        v3_125.v8_242((v11_792.v7_328, v12_858))
                    if v11_792.v9_854:
                        v3_125.v8_242((v11_792.v9_854, v12_858))
                    break
            if not v12_858:
                return True
        return False