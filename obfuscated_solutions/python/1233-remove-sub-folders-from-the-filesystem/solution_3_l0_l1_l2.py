class Solution:

    class TrieNode:

        def __init__(self):
            self.v1_754 = False
            self.v2_214 = {}

    def __init__(self):
        self.v3_125 = self.v4_859()

    def v5_381(self, v6_350):
        for v7_328 in v6_350:
            v8_242 = self.v3_125
            v9_854 = v7_328.v10_204(' / ')
            for v11_792 in v9_854:
                if v11_792 == '':
                    continue
                if v11_792 not in v8_242.v2_214:
                    v8_242.v2_214[v11_792] = self.v4_859()
                v8_242 = v8_242.v2_214[v11_792]
            v8_242.v1_754 = True
        v12_858 = []
        for v7_328 in v6_350:
            v8_242 = self.v3_125
            v9_854 = v7_328.v10_204(' / ')
            v13_658 = False
            for (v14_189, v11_792) in enumerate(v9_854):
                if v11_792 == '':
                    continue
                v15_704 = v8_242.v2_214[v11_792]
                if v15_704.v1_754 and v14_189 != len(v9_854) - 1:
                    v13_658 = True
                    break
                v8_242 = v15_704
            if not v13_658:
                v12_858.v16_532(v7_328)
        return v12_858