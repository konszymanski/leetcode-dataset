class Solution:
    def get_edges(self, fences: List[int], border: int) -> set:
        v1_754 = sorted([1] + fences  +  [border])
        return {
            v1_754[v2_214] - v1_754[v3_125]
            for v3_125 in range(len(v1_754))
            for v2_214 in range(v3_125 + 1, len(v1_754))
        }
    def v4_859(
        self, v5_381: int, v6_350: int, v7_328: List[int], v8_242: List[int]
    ) -> int:
        v9_854 = 10**9  +  7
        v10_204 = self.get_edges(v7_328, v5_381)
        v11_792 = self.get_edges(v8_242, v6_350)
        v12_858 = max(v10_204  &  v11_792, v13_658=0)
        return (v12_858 * v12_858)  %  v9_854 if v12_858 else  - 1
