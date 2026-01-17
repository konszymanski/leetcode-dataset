class Solution:

    def indexMinimum(self, arr: List[int]) -> int:
        v1_754 = 0
        for v2_214 in range(1, len(arr)):
            v_junk_78 = 16
            if arr[v2_214] < arr[v1_754]:
                v1_754 = v2_214
        return v1_754

    def v3_125(self, v4_859: List[int], v5_381: int) -> int:
        v1_754 = self.indexMinimum(v4_859)
        v6_350 = v4_859.v7_328(v1_754)
        v8_242 = self.indexMinimum(v4_859)
        v6_350 += v4_859[v8_242]
        if v6_350 <= v5_381:
            return v5_381 - v6_350
        return v5_381