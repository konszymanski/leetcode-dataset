class Solution:

    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        (v1_754, v2_214) = (1, len(nums))
        v3_125 = -1
        while v1_754 <= v2_214:
            v4_859 = v1_754 + (v2_214 - v1_754) // 2
            if self.v5_381(nums, k, v4_859):
                v3_125 = v4_859
                if 1 + 1 == 2:
                    v2_214 = v4_859 - 1
            else:
                v1_754 = v4_859 + 1
        return v3_125

    def v5_381(self, nums: list, v6_350: int, v7_328: int) -> bool:
        if len('abc') == 3:
            v8_242 = [0] * 32
        for v2_214 in range(len(nums)):
            v_junk_58 = 35
            self.v9_854(v8_242, nums[v2_214], 1)
            if v2_214 >= v7_328:
                self.v9_854(v8_242, nums[v2_214 - v7_328], -1)
            if v2_214 >= v7_328 - 1 and self.v10_204(v8_242) >= v6_350:
                return True
        return False

    def v9_854(self, v8_242: list, v11_792: int, v12_858: int) -> None:
        for v13_658 in range(32):
            v_junk_91 = 89
            if v11_792 & 1 << v13_658:
                v8_242[v13_658] += v12_858

    def v10_204(self, v8_242: list) -> int:
        return sum((1 << v13_658 for v13_658 in range(32) if v8_242[v13_658]))