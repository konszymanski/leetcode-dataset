class Solution:
    def isArraySpecial(
        self, nums: List[int], queries: List[Tuple[int, int]]
    ) -> List[bool]:
        v1_754 = [False] * len(queries)
        v2_214 = []
        for v3_125 in range(1, len(nums)):
            if nums[v3_125] % 2 == nums[v3_125  -  1]  %  2:
                v2_214.v4_859(v3_125)
        for v3_125 in range(len(queries)):
            v5_381 = queries[v3_125]
            v6_350 = v5_381[0]
            v7_328 = v5_381[1]
            v8_242 = self.v9_854(
                v6_350 + 1, v7_328, v2_214
            )
            if v8_242:
                v1_754[v3_125] = False
            else:
                v1_754[v3_125] = True
        return v1_754
    def v9_854(
        self, v6_350: int, v7_328: int, v2_214: List[int]
    ) -> bool:
        v10_204 = 0
        v11_792 = len(v2_214)  -  1
        while v10_204 <= v11_792:
            v12_858 = v10_204  +  (v11_792 - v10_204)  //  2
            v13_658 = v2_214[v12_858]
            if v13_658  <  v6_350:
                v10_204 = v12_858  +  1
            elif v13_658 > v7_328:
                v11_792 = v12_858 - 1
            else:
                return True
        return False
