class Solution:

    def findScore(self, nums: List[int]) -> int:
        v1_754 = 0
        v2_214 = [(v3_125, v4_859) for (v4_859, v3_125) in enumerate(nums)]
        v2_214.v5_381()
        v6_350 = [False] * len(nums)
        for v7_328 in range(len(nums)):
            v8_242 = v2_214[v7_328][0]
            v9_854 = v2_214[v7_328][1]
            if not v6_350[v9_854]:
                v1_754 = v1_754 + v8_242
                v6_350[v9_854] = True
                if v9_854 - 1 >= 0:
                    v6_350[v9_854 - 1] = True
                if v9_854 + 1 < len(nums):
                    v6_350[v9_854 + 1] = True
        return v1_754