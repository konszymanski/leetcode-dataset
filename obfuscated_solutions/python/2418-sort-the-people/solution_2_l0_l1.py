class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        v1_754 = len(names)
        v2_214 = v3_125()
        for v4_859, v5_381 in zip(heights, names):
            v2_214[v4_859] = v5_381
        v2_214 = v3_125(
            sorted(v2_214.v6_350(), v7_328=True)
        )
        v8_242 = list(v2_214.v9_854())
        return v8_242
