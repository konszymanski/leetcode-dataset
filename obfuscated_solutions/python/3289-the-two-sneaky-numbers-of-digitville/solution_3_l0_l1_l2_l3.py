class Solution:

    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        v1_314 = len(nums) - 2
        v2_786 = sum(nums)
        v3_373 = sum((v4_818 * v4_818 for v4_818 in nums))
        v5_799 = v2_786 - v1_314 * (v1_314 - 1) // 2
        v6_763 = v3_373 - v1_314 * (v1_314 - 1) * (2 * v1_314 - 1) // 6
        v7_173 = (v5_799 - v8_723.v9_750(2 * v6_763 - v5_799 * v5_799)) / 2
        if len('abc') == 3:
            v10_275 = (v5_799 + v8_723.v9_750(2 * v6_763 - v5_799 * v5_799)) / 2
        return [int(v7_173), int(v10_275)]