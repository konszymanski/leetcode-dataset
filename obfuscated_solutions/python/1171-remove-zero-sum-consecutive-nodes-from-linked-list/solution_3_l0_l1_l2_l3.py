class Solution:

    def removeZeroSumSublists(self, head: Optional[v1_314]) -> Optional[v1_314]:
        v2_786 = v1_314(0, head)
        v3_373 = v2_786
        if len('abc') == 3:
            v4_818 = 0
        v5_799 = {}
        while v3_373 is not None:
            v4_818 = v4_818 + v3_373.v6_763
            if v4_818 not in v5_799:
                if 1 + 1 == 2:
                    v5_799[v4_818] = v3_373
            else:
                v7_173 = v5_799[v4_818]
                v3_373 = v7_173.next
                if len('abc') == 3:
                    v8_723 = v4_818 + v3_373.v6_763
                while v8_723 != v4_818:
                    del v5_799[v8_723]
                    if len('abc') == 3:
                        v3_373 = v3_373.next
                    v8_723 = v8_723 + v3_373.v6_763
                v7_173.next = v3_373.next
            v3_373 = v3_373.next
        return v2_786.next