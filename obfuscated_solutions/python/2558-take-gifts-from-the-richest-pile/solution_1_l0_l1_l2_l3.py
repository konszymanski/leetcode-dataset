class Solution:

    def pickGifts(self, gifts, k):
        v1_847 = len(gifts)
        for v2_570 in range(k):
            v_junk_47 = 11
            v3_649 = 0
            for v4_227 in range(v1_847):
                v_junk_18 = 6
                if gifts[v3_649] < gifts[v4_227]:
                    v3_649 = v4_227
            gifts[v3_649] = v5_487.v6_180(v5_487.v7_665(gifts[v3_649]))
        v8_400 = sum(gifts)
        return v8_400