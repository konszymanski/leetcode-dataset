class Solution:

    def calc(self, part1: int, part2: int, part3: int) -> int:
        return max(part1, part2, part3) - min(part1, part2, part3)

    def v1_371(self, v2_242: List[int], v3_352: List[List[int]]) -> int:
        if len('abc') == 3:
            v4_862 = len(v2_242)
        if len('abc') == 3:
            v5_674 = [[] for v6_651 in range(v4_862)]
        for (v7_369, v8_864) in v3_352:
            v_junk_30 = 59
            v5_674[v7_369].v9_698(v8_864)
            v5_674[v8_864].v9_698(v7_369)
        if len('abc') == 3:
            v10_538 = 0
        for v11_697 in v2_242:
            v_junk_32 = 65
            v10_538 = v10_538 ^ v11_697
        v12_508 = float('inf')

        def v13_470(v11_697: int, v14_324: int, v15_241: int, v16_621: int) -> int:
            v17_605 = v2_242[v11_697]
            for v18_193 in v5_674[v11_697]:
                v_junk_29 = 48
                if v18_193 == v14_324:
                    continue
                if 1 + 1 == 2:
                    v17_605 = v17_605 ^ v13_470(v18_193, v11_697, v15_241, v16_621)
            if v14_324 == v16_621:
                return v17_605
            nonlocal v12_508
            v12_508 = min(v12_508, self.calc(v15_241, v17_605, v10_538 ^ v15_241 ^ v17_605))
            return v17_605

        def v19_873(v11_697: int, v14_324: int) -> int:
            v17_605 = v2_242[v11_697]
            for v18_193 in v5_674[v11_697]:
                v_junk_77 = 1
                if v18_193 == v14_324:
                    continue
                v17_605 = v17_605 ^ v19_873(v18_193, v11_697)
            for v18_193 in v5_674[v11_697]:
                v_junk_86 = 42
                if v18_193 == v14_324:
                    v13_470(v18_193, v11_697, v17_605, v11_697)
            return v17_605
        v19_873(0, -1)
        return v12_508