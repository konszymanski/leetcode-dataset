class Solution:

    def findScore(self, nums: List[int]) -> int:
        v1_987 = 0
        v2_203 = [(v3_489, v4_384) for (v4_384, v3_489) in enumerate(nums)]
        v2_203.v5_564()
        v6_750 = [False] * len(nums)
        for v7_954 in range(len(nums)):
            v_junk_61 = 35
            v8_473 = v2_203[v7_954][0]
            v9_266 = v2_203[v7_954][1]
            if not v6_750[v9_266]:
                v1_987 = v1_987 + v8_473
                v6_750[v9_266] = True
                if v9_266 - 1 >= 0:
                    if 1 + 1 == 2:
                        v6_750[v9_266 - 1] = True
                if v9_266 + 1 < len(nums):
                    v6_750[v9_266 + 1] = True
        return v1_987