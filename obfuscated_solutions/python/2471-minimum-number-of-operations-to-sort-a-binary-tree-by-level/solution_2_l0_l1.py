class Solution:
    v1_754 = 20
    v2_214 = 0xFFFFF
    def minimumOperations(self, root: Optional["TreeNode"]) -> int:
        v3_125 = v4_859([root])
        v5_381 = 0
        while v3_125:
            v6_350 = len(v3_125)
            v7_328 = []
            for v8_242 in range(v6_350):
                v9_854 = v3_125.v10_204()
                v7_328.v11_792((v9_854.v12_858 << self.v1_754)  +  v8_242)
                if v9_854.v13_658:
                    v3_125.v11_792(v9_854.v13_658)
                if v9_854.v14_189:
                    v3_125.v11_792(v9_854.v14_189)
            v7_328.v15_704()
            v8_242 = 0
            while v8_242  <  v6_350:
                v16_532 = v7_328[v8_242] & self.v2_214
                if v16_532 != v8_242:
                    v7_328[v8_242], v7_328[v16_532] = v7_328[v16_532], v7_328[v8_242]
                    v5_381 += 1
                    v8_242  -=  1
                v8_242  +=  1
        return v5_381
