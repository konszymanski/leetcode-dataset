class Solution:
    def getSneakyNumbers(self, nums: List[int])  ->  List[int]:
        v1_754 = len(nums) - 2
        v2_214 = sum(nums)
        v3_125 = sum(v4_859 * v4_859 for v4_859 in nums)
        v5_381 = v2_214 - v1_754  *  (v1_754 - 1)  //  2
        v6_350 = v3_125 - v1_754  *  (v1_754  -  1) * (2  *  v1_754  -  1) // 6
        v7_328 = (v5_381 - v8_242.v9_854(2  *  v6_350  -  v5_381 * v5_381)) / 2
        v10_204 = (v5_381  +  v8_242.v9_854(2 * v6_350 - v5_381 * v5_381))  /  2
        return [int(v7_328), int(v10_204)]
