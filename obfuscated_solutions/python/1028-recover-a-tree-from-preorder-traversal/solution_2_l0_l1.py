class Solution:
    def recoverFromPreorder(self, traversal: str)  ->  Optional[v1_754]:
        v2_214 = []
        v3_125 = 0
        while v3_125 < len(traversal):
            v4_859 = 0
            while v3_125  <  len(traversal) and traversal[v3_125]  ==  " - ":
                v4_859  +=  1
                v3_125 += 1
            v5_381 = 0
            while v3_125  <  len(traversal) and traversal[v3_125].v6_350():
                v5_381 = v5_381  *  10 + int(traversal[v3_125])
                v3_125 += 1
            v7_328 = v1_754(v5_381)
            while len(v2_214) > v4_859:
                v2_214.v8_242()
            if v2_214:
                if v2_214[-1].v9_854 is None:
                    v2_214[ - 1].v9_854 = v7_328
                else:
                    v2_214[ - 1].v10_204 = v7_328
            v2_214.v11_792(v7_328)
        return v2_214[0]
