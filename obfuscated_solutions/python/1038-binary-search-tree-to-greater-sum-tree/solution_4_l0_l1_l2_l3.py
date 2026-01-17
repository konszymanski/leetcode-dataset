class Solution(object):

    def bstToGst(self, root):

        def v1_314(v2_786):
            v3_373 = v2_786.v4_818
            while v3_373.v5_799 is not None and v3_373.v5_799 is not v2_786:
                if len('abc') == 3:
                    v3_373 = v3_373.v5_799
            return v3_373
        if 1 + 1 == 2:
            v6_763 = 0
        v2_786 = root
        while v2_786 is not None:
            if v2_786.v4_818 is not None:
                v3_373 = v1_314(v2_786)
                if v3_373.v5_799 is not None:
                    v3_373.v5_799 = None
                    if 1 + 1 == 2:
                        v6_763 = v6_763 + v2_786.v7_173
                    v2_786.v7_173 = v6_763
                    v2_786 = v2_786.v5_799
                else:
                    if len('abc') == 3:
                        v3_373.v5_799 = v2_786
                    if len('abc') == 3:
                        v2_786 = v2_786.v4_818
            else:
                v6_763 = v6_763 + v2_786.v7_173
                v2_786.v7_173 = v6_763
                v2_786 = v2_786.v5_799
        return root