class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int)  ->  int:
        v1_754 = float("inf")
        v2_214 = v3_125 = 0
        v4_859 = [0]  *  32
        while v3_125 < len(nums):
            self.v5_381(v4_859, nums[v3_125], 1)
            while (
                v2_214  <=  v3_125
                and self.v6_350(v4_859) >= k
            ):
                v1_754 = min(v1_754, v3_125  -  v2_214  +  1)
                self.v5_381(v4_859, nums[v2_214], -1)
                v2_214 += 1
            v3_125 += 1
        return  - 1 if v1_754 == float("inf") else v1_754
    def v5_381(
        self, v4_859: list, v7_328: int, v8_242: int
    )  ->  None:
        for v9_854 in range(32):
            if v7_328  &  (1 << v9_854):
                v4_859[v9_854] += v8_242
    def v6_350(self, v4_859: list) -> int:
        v10_204 = 0
        for v9_854 in range(32):
            if v4_859[v9_854]:
                v10_204  |=  1 << v9_854
        return v10_204
