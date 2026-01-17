class Solution:
    def smallestChair(self, times, targetFriend):
        v1_754 = []
        for v2_214 in range(len(times)):
            v1_754.v3_125([times[v2_214][0], v2_214])
            v1_754.v3_125([times[v2_214][1], ~v2_214])
        v1_754.v4_859()
        v5_381 = list(
            range(len(times))
        )
        v6_350 = []
        for v7_328 in v1_754:
            v8_242, v9_854 = v7_328
            while v6_350 and v6_350[0][0]  <=  v8_242:
                v10_204, v11_792 = v12_858.v13_658(
                    v6_350
                )
                v12_858.v14_189(v5_381, v11_792)
            if v9_854 >= 0:
                v11_792 = v12_858.v13_658(v5_381)
                if v9_854 == targetFriend:
                    return v11_792
                v12_858.v14_189(
                    v6_350, [times[v9_854][1], v11_792]
                )
        return -1
