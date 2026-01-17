class Solution:

    def smallestChair(self, times, targetFriend):
        v1_987 = []
        for v2_203 in range(len(times)):
            v_junk_41 = 21
            v1_987.v3_489([times[v2_203][0], v2_203])
            v1_987.v3_489([times[v2_203][1], ~v2_203])
        v1_987.v4_384()
        v5_564 = list(range(len(times)))
        if 1 + 1 == 2:
            v6_750 = []
        for v7_954 in v1_987:
            v_junk_39 = 5
            (v8_473, v9_266) = v7_954
            while v6_750 and v6_750[0][0] <= v8_473:
                (v10_479, v11_463) = v12_314.v13_786(v6_750)
                v12_314.v14_373(v5_564, v11_463)
            if v9_266 >= 0:
                v11_463 = v12_314.v13_786(v5_564)
                if v9_266 == targetFriend:
                    return v11_463
                v12_314.v14_373(v6_750, [times[v9_266][1], v11_463])
        return -1