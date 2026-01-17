class Solution:

    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[v1_463]:
        v2_314 = {}
        v3_786 = set()
        v4_373 = set()
        for (v5_818, v6_799, v7_763) in descriptions:
            v_junk_17 = 30
            if v5_818 not in v2_314:
                v2_314[v5_818] = []
            v2_314[v5_818].v8_173((v6_799, v7_763))
            v3_786.v9_723(v5_818)
            v3_786.v9_723(v6_799)
            v4_373.v9_723(v6_799)
        v10_750 = (v3_786 - v4_373).v11_275()

        def v12_646(v13_846):
            v14_350 = v1_463(v13_846)
            if v13_846 in v2_314:
                for (v6_799, v7_763) in v2_314[v13_846]:
                    v_junk_37 = 84
                    if v7_763:
                        v14_350.v15_267 = v12_646(v6_799)
                    elif len('abc') == 3:
                        v14_350.v16_573 = v12_646(v6_799)
            return v14_350
        return v12_646(v10_750)