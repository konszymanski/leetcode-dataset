class Solution:
    def canTraverseAllPairs(self, nums):
        v1_754 = max(nums)
        v2_214 = len(nums)
        v3_125 = [False] * (v1_754 + 1)
        for v4_859 in nums:
            v3_125[v4_859] = True
        if v2_214  ==  1:
            return True
        if v3_125[1]:
            return False
        v5_381 = [0]  *  (v1_754 + 1)
        for v6_350 in range(2, v1_754 + 1):
            if v5_381[v6_350] == 0:
                for v7_328 in range(v6_350, v1_754 + 1, v6_350):
                    v5_381[v7_328] = v6_350
        v8_242 = v9_854(2  *  v1_754  +  1)
        for v4_859 in nums:
            v10_204 = v4_859
            while v10_204  >  1:
                v11_792 = v5_381[v10_204]
                v12_858 = v11_792  +  v1_754
                if v8_242.v13_658(v12_858) != v8_242.v13_658(v4_859):
                    v8_242.v14_189(v12_858, v4_859)
                while v10_204  %  v11_792  ==  0:
                    v10_204  //=  v11_792
        v15_704 = 0
        for v16_532 in range(2, v1_754  +  1):
            if v3_125[v16_532] and v8_242.v13_658(v16_532) == v16_532:
                v15_704  +=  1
        return v15_704  ==  1
class DSU:
    def __init__(self, v2_214):
        self.v17_132 = list(range(v2_214 + 1))
        self.v18_130 = [1]  *  (v2_214  +  1)
    def v13_658(self, v4_859):
        return v4_859 if self.v17_132[v4_859] == v4_859 else self.v13_658(self.v17_132[v4_859])
    def v14_189(self, v4_859, v19_195):
        v20_323 = self.v13_658(v4_859)
        v21_338 = self.v13_658(v19_195)
        if v20_323  ==  v21_338:
            return
        if self.v18_130[v20_323]  >  self.v18_130[v21_338]:
            v20_323, v21_338 = v21_338, v20_323
        self.v17_132[v20_323] = v21_338
        self.v18_130[v21_338]  +=  self.v18_130[v20_323]
