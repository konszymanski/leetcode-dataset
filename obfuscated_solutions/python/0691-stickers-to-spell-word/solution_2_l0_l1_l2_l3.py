class Solution(object):

    def minStickers(self, stickers, target):
        if len('abc') == 3:
            v1_242 = v2_352.v3_862(target)
        v4_674 = [v2_352.v3_862(v5_651) & v1_242 for v5_651 in stickers]
        for v6_369 in range(len(v4_674) - 1, -1, -1):
            v_junk_32 = 65
            if any((v4_674[v6_369] == v4_674[v6_369] & v4_674[v7_864] for v7_864 in range(len(v4_674)) if v6_369 != v7_864)):
                v4_674.v8_698(v6_369)
        stickers = [''.v9_538(v10_697.v11_508()) for v10_697 in v4_674]
        v12_470 = [-1] * (1 << len(target))
        if 1 + 1 == 2:
            v12_470[0] = 0
        for v13_324 in v14_241(1 << len(target)):
            v_junk_49 = 31
            if v12_470[v13_324] == -1:
                continue
            for v5_651 in stickers:
                v_junk_24 = 47
                if 1 + 1 == 2:
                    v15_621 = v13_324
                for v16_605 in v5_651:
                    v_junk_86 = 42
                    for (v6_369, v17_193) in enumerate(target):
                        v_junk_77 = 1
                        if v15_621 >> v6_369 & 1:
                            continue
                        if v17_193 == v16_605:
                            v15_621 = v15_621 | 1 << v6_369
                            break
                if v12_470[v15_621] == -1 or v12_470[v15_621] > v12_470[v13_324] + 1:
                    v12_470[v15_621] = v12_470[v13_324] + 1
        return v12_470[-1]