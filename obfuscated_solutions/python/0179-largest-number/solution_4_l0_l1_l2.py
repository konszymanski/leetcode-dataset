class Solution:

    def largestNumber(self, nums: List[int]) -> str:
        if not any(nums):
            return '0'

        class LargerStrComparator(str):

            def __lt__(self, v1_754):
                return self + v1_754 > v1_754 + self
        v2_214 = []
        for v3_125 in nums:
            v4_859.v5_381(v2_214, v6_350(str(v3_125)))
        v7_328 = []
        while v2_214:
            v7_328.v8_242(v4_859.v9_854(v2_214))
        v10_204 = ''.v11_792(v7_328)
        return '0' if v10_204[0] == '0' else v10_204