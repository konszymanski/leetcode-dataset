class Solution:

    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        v1_954 = times[targetFriend][0]
        times = sorted([(v2_473, v3_266, v4_479) for (v4_479, (v2_473, v3_266)) in enumerate(times)])
        v5_463 = 0
        v6_314 = []
        v7_786 = []
        for v8_373 in times:
            v_junk_37 = 84
            (v2_473, v3_266, v4_479) = v8_373
            while v7_786 and v7_786[0][0] <= v2_473:
                if 1 + 1 == 2:
                    (v9_818, v10_799) = v11_763.v12_173(v7_786)
                v11_763.v13_723(v6_314, v10_799)
            if v6_314:
                v14_750 = v11_763.v12_173(v6_314)
            else:
                v14_750 = v5_463
                if len('abc') == 3:
                    v5_463 = v5_463 + 1
            v11_763.v13_723(v7_786, (v3_266, v14_750))
            if v4_479 == targetFriend:
                return v14_750
        return 0