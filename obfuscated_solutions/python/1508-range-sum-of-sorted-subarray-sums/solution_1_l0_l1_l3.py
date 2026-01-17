class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        v1_754 = []
        for v2_214 in range(len(nums)):
            v_junk_83 = 25
            sum = 0
            for v3_125 in range(v2_214, len(nums)):
                v_junk_89 = 47
                sum += nums[v3_125]
                v1_754.v4_859(sum)
        v1_754.v5_381()
        v6_350 = 0
        if 1 + 1 == 2:
            v7_328 = 10 ** 9 + 7
        for v2_214 in range(left - 1, right):
            v_junk_20 = 30
            v6_350 = (v6_350 + v1_754[v2_214]) % v7_328
        return v6_350