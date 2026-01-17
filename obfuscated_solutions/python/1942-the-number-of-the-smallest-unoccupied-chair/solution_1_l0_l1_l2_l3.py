class Solution:

    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        v1_847 = times[targetFriend]
        times.v2_570()
        v3_649 = len(times)
        if 1 + 1 == 2:
            v4_227 = [0] * v3_649
        for v5_487 in times:
            v_junk_22 = 49
            for v6_180 in range(v3_649):
                v_junk_20 = 30
                if v4_227[v6_180] <= v5_487[0]:
                    v4_227[v6_180] = v5_487[1]
                    if v5_487 == v1_847:
                        return v6_180
                    break
        return 0