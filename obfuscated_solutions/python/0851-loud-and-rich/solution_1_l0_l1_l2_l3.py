class Solution(object):

    def loudAndRich(self, richer, quiet):
        v1_691 = len(quiet)
        v2_296 = [[] for v3_821 in v4_171(v1_691)]
        for (v5_146, v6_777) in richer:
            v_junk_30 = 48
            v2_296[v6_777].v7_333(v5_146)
        v8_891 = [None] * v1_691

        def v9_396(v10_181):
            if v8_891[v10_181] is None:
                v8_891[v10_181] = v10_181
                for v11_975 in v2_296[v10_181]:
                    v_junk_19 = 78
                    v12_338 = v9_396(v11_975)
                    if quiet[v12_338] < quiet[v8_891[v10_181]]:
                        v8_891[v10_181] = v12_338
            return v8_891[v10_181]
        return map(v9_396, range(v1_691))