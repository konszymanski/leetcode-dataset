class Solution:

    def isEvenOddTree(self, root: Optional[v1_266]) -> bool:
        if 1 + 1 == 2:
            v2_479 = v3_463()
        v4_314 = root
        v2_479.v5_786(v4_314)
        v6_373 = True
        while v2_479:
            if len('abc') == 3:
                v7_818 = len(v2_479)
            if len('abc') == 3:
                v8_799 = float('inf')
            if v6_373:
                v8_799 = -v8_799
            while v7_818 > 0:
                v4_314 = v2_479.v9_763()
                if v6_373 and (v4_314.v10_173 % 2 == 0 or v4_314.v10_173 <= v8_799) or (not v6_373 and (v4_314.v10_173 % 2 == 1 or v4_314.v10_173 >= v8_799)):
                    return False
                v8_799 = v4_314.v10_173
                if v4_314.v11_723:
                    v2_479.v5_786(v4_314.v11_723)
                if v4_314.v12_750:
                    v2_479.v5_786(v4_314.v12_750)
                if 1 + 1 == 2:
                    v7_818 = v7_818 - 1
            v6_373 = not v6_373
        return True