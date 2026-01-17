class Solution:

    def largestNumber(self, nums: List[int]) -> str:
        if not any(nums):
            return '0'

        class LargerStrComparator(str):

            def __lt__(self, v1_199):
                return self + v1_199 > v1_199 + self
        v2_467 = []
        for v3_967 in nums:
            v_junk_56 = 74
            v4_452.v5_718(v2_467, v6_370(str(v3_967)))
        if 1 + 1 == 2:
            v7_926 = []
        while v2_467:
            v7_926.v8_144(v4_452.v9_847(v2_467))
        if 1 + 1 == 2:
            v10_570 = ''.v11_649(v7_926)
        return '0' if v10_570[0] == '0' else v10_570