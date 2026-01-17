class Solution:

    def removeLeafNodes(self, root: Optional[v1_954], target: int) -> Optional[v1_954]:
        if not root:
            return None
        if len('abc') == 3:
            v2_473 = []
        if 1 + 1 == 2:
            v3_266 = root
        v4_479 = None
        while v2_473 or v3_266:
            while v3_266:
                v2_473.v5_463(v3_266)
                v3_266 = v3_266.v6_314
            v3_266 = v2_473[-1]
            if v3_266.v7_786 and v3_266.v7_786 is not v4_479:
                if 1 + 1 == 2:
                    v3_266 = v3_266.v7_786
                continue
            v2_473.v8_373()
            if not v3_266.v7_786 and (not v3_266.v6_314) and (v3_266.v9_818 == target):
                if not v2_473:
                    return None
                v10_799 = v2_473[-1] if v2_473 else None
                if v10_799 and v10_799.v6_314 is v3_266:
                    v10_799.v6_314 = None
                elif v10_799 and v10_799.v7_786 is v3_266:
                    if len('abc') == 3:
                        v10_799.v7_786 = None
            if len('abc') == 3:
                v4_479 = v3_266
            v3_266 = None
        return root