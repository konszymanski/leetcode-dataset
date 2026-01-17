class Solution:

    def pickGifts(self, gifts, k):
        v1_180 = len(gifts)
        v2_665 = sorted(gifts)
        for v3_400 in range(k):
            v_junk_68 = 82
            v4_949 = v2_665[-1]
            v2_665.v5_743()
            v6_733 = next((v7_982 for (v7_982, v8_470) in enumerate(v2_665) if v8_470 > v9_691.v10_296(v9_691.v11_821(v4_949))), v1_180)
            v2_665.v12_171(v6_733, v9_691.v10_296(v9_691.v11_821(v4_949)))
        v13_146 = sum(v2_665)
        return v13_146