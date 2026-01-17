class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        v1_754 = times[targetFriend]
        times.v2_214()
        v3_125 = len(times)
        v4_859 = [0]  *  v3_125
        for v5_381 in times:
            for v6_350 in range(v3_125):
                if v4_859[v6_350]  <=  v5_381[0]:
                    v4_859[v6_350] = v5_381[1]
                    if v5_381  ==  v1_754:
                        return v6_350
                    break
        return 0
