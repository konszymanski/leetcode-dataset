class Solution:
    def v1_754(self, v2_214: List[List[str]])  ->  List[List[str]]:
        v3_125 = len(v2_214)
        v4_859 = len(v2_214[0])
        v5_381 = [["" for v6_350 in range(v3_125)] for v6_350 in range(v4_859)]
        for v7_328 in range(v4_859):
            for v8_242 in range(v3_125):
                v5_381[v7_328][v8_242] = v2_214[v8_242][v7_328]
        for v7_328 in range(v4_859):
            v5_381[v7_328].v9_854()
        for v8_242 in range(v3_125):
            for v7_328 in range(v4_859 - 1,  - 1,  - 1):
                if (
                    v5_381[v7_328][v8_242]  ==  "."
                ):
                    v10_204 =  - 1
                    for v11_792 in range(v7_328  -  1, -1, -1):
                        if v5_381[v11_792][v8_242]  ==  "*":
                            break
                        if (
                            v5_381[v11_792][v8_242] == "
                        ):
                            v10_204 = v11_792
                            break
                    if v10_204 !=  - 1:
                        v5_381[v10_204][v8_242] = "."
                        v5_381[v7_328][v8_242] = "
        return v5_381
