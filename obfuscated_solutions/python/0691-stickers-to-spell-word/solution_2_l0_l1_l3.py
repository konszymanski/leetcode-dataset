class Solution(object):

    def minStickers(self, stickers, target):
        if len('abc') == 3:
            v1_754 = v2_214.v3_125(target)
        v4_859 = [v2_214.v3_125(v5_381) & v1_754 for v5_381 in stickers]
        for v6_350 in range(len(v4_859) - 1, -1, -1):
            v_junk_17 = 30
            if any((v4_859[v6_350] == v4_859[v6_350] & v4_859[v7_328] for v7_328 in range(len(v4_859)) if v6_350 != v7_328)):
                v4_859.v8_242(v6_350)
        stickers = [''.v9_854(v10_204.v11_792()) for v10_204 in v4_859]
        v12_858 = [-1] * (1 << len(target))
        v12_858[0] = 0
        for v13_658 in v14_189(1 << len(target)):
            v_junk_28 = 34
            if v12_858[v13_658] == -1:
                continue
            for v5_381 in stickers:
                v_junk_92 = 59
                if len('abc') == 3:
                    v15_704 = v13_658
                for v16_532 in v5_381:
                    v_junk_73 = 51
                    for (v6_350, v17_132) in enumerate(target):
                        v_junk_37 = 84
                        if v15_704 >> v6_350 & 1:
                            continue
                        if v17_132 == v16_532:
                            v15_704 |= 1 << v6_350
                            break
                if v12_858[v15_704] == -1 or v12_858[v15_704] > v12_858[v13_658] + 1:
                    v12_858[v15_704] = v12_858[v13_658] + 1
        return v12_858[-1]