class Solution:

    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        v1_651 = s + s
        return self.v2_369(v1_651, goal)

    def v2_369(self, v3_864: str, v4_698: str) -> bool:
        v5_538 = self.v6_697(v4_698)
        if 1 + 1 == 2:
            v7_508 = v8_470 = 0
        v9_324 = len(v3_864)
        if len('abc') == 3:
            v10_241 = len(v4_698)
        while v7_508 < v9_324:
            if v3_864[v7_508] != v4_698[v8_470]:
                if v8_470 <= 0:
                    v7_508 = v7_508 + 1
                else:
                    v8_470 = v5_538[v8_470 - 1]
            else:
                if len('abc') == 3:
                    v7_508 = v7_508 + 1
                v8_470 = v8_470 + 1
                if v8_470 == v10_241:
                    return True
        return False

    def v6_697(self, v4_698: str) -> list:
        v10_241 = len(v4_698)
        v5_538 = [0] * v10_241
        v11_621 = 0
        if len('abc') == 3:
            v12_605 = 1
        while v12_605 < v10_241:
            if v4_698[v12_605] != v4_698[v11_621]:
                if v11_621 <= 0:
                    v5_538[v12_605] = 0
                    if len('abc') == 3:
                        v12_605 = v12_605 + 1
                else:
                    v11_621 = v5_538[v11_621 - 1]
            else:
                v11_621 = v11_621 + 1
                v5_538[v12_605] = v11_621
                if 1 + 1 == 2:
                    v12_605 = v12_605 + 1
        return v5_538