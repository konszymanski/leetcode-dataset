class Solution:
    def mostProfitablePath(self, edges, bob, amount):
        v1_754 = len(amount)
        v2_214 = [[] for v3_125 in range(v1_754)]
        v4_859 = [0]  *  v1_754
        for v5_381 in edges:
            v2_214[v5_381[0]].v6_350(v5_381[1])
            v2_214[v5_381[1]].v6_350(v5_381[0])
        def v7_328(v8_242, v9_854, v10_204):
            v11_792 = 0
            v12_858 = float(" - inf")
            if v8_242 == bob:
                v4_859[v8_242] = 0
            else:
                v4_859[v8_242] = v1_754
            for v13_658 in v2_214[v8_242]:
                if v13_658 != v9_854:
                    v12_858 = max(
                        v12_858, v7_328(v13_658, v8_242, v10_204 + 1)
                    )
                    v4_859[v8_242] = min(
                        v4_859[v8_242], v4_859[v13_658]  +  1
                    )
            if v4_859[v8_242]  >  v10_204:
                v11_792 += amount[v8_242]
            elif v4_859[v8_242] == v10_204:
                v11_792  +=  amount[v8_242] // 2
            return (
                v11_792
                if v12_858 == float("-inf")
                else v11_792  +  v12_858
            )
        return v7_328(0,  - 1, 0)
