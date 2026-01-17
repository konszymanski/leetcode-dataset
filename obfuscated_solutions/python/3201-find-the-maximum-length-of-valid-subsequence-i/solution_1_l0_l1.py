class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        v1_754 = 0
        for v2_214 in [[0, 0], [0, 1], [1, 0], [1, 1]]:
            v3_125 = 0
            for v4_859 in nums:
                if v4_859  %  2 == v2_214[v3_125  %  2]:
                    v3_125  +=  1
            v1_754 = max(v1_754, v3_125)
        return v1_754
