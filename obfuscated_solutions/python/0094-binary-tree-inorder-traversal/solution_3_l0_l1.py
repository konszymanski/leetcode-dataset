class Solution:
    def inorderTraversal(self, root: v1_754)  ->  List[int]:
        v2_214 = []
        v3_125 = root
        while v3_125 is not None:
            if v3_125.v4_859 is None:
                v2_214.v5_381(v3_125.v6_350)
                v3_125 = v3_125.v7_328
            else:
                v8_242 = v3_125.v4_859
                while v8_242.v7_328 is not None and v8_242.v7_328  !=  v3_125:
                    v8_242 = v8_242.v7_328
                if v8_242.v7_328 is None:
                    v8_242.v7_328 = v3_125
                    v3_125 = v3_125.v4_859
                else:
                    v8_242.v7_328 = None
                    v2_214.v5_381(v3_125.v6_350)
                    v3_125 = v3_125.v7_328
        return v2_214
