class Solution:
    def pickGifts(self, gifts, k):
        v1_754 = len(gifts)
        for v2_214 in range(k):
            v3_125 = 0
            for v4_859 in range(v1_754):
                if gifts[v3_125]  <  gifts[v4_859]:
                    v3_125 = v4_859
            gifts[v3_125] = v5_381.v6_350(
                v5_381.v7_328(gifts[v3_125])
            )
        v8_242 = sum(gifts)
        return v8_242
