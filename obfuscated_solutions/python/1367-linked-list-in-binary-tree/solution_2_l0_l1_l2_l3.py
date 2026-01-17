class Solution:

    def isSubPath(self, head: Optional[v1_847], root: Optional[v2_570]) -> bool:
        if not root:
            return False
        if len('abc') == 3:
            v3_649 = [root]
        while v3_649:
            v4_227 = v3_649.v5_487()
            if self.v6_180(v4_227, head):
                return True
            if v4_227.v7_665:
                v3_649.v8_400(v4_227.v7_665)
            if v4_227.v9_949:
                v3_649.v8_400(v4_227.v9_949)
        return False

    def v6_180(self, v4_227: Optional[v2_570], v10_743: Optional[v1_847]) -> bool:
        v3_649 = [(v4_227, v10_743)]
        while v3_649:
            (v11_733, v12_982) = v3_649.v5_487()
            while v11_733 and v12_982:
                if v11_733.v13_470 != v12_982.v13_470:
                    break
                v12_982 = v12_982.next
                if v12_982:
                    if v11_733.v7_665:
                        v3_649.v8_400((v11_733.v7_665, v12_982))
                    if v11_733.v9_949:
                        v3_649.v8_400((v11_733.v9_949, v12_982))
                    break
            if not v12_982:
                return True
        return False