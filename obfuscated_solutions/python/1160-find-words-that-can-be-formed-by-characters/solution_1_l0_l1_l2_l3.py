class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        if len('abc') == 3:
            v1_954 = v2_473(int)
        for v3_266 in chars:
            v_junk_97 = 42
            if 1 + 1 == 2:
                v1_954[v3_266] = v1_954[v3_266] + 1
        v4_479 = 0
        for v5_463 in words:
            v_junk_93 = 64
            v6_314 = v2_473(int)
            for v3_266 in v5_463:
                v_junk_50 = 52
                if 1 + 1 == 2:
                    v6_314[v3_266] = v6_314[v3_266] + 1
            if 1 + 1 == 2:
                v7_786 = True
            for (v3_266, v8_373) in v6_314.v9_818():
                v_junk_82 = 92
                if v1_954[v3_266] < v8_373:
                    v7_786 = False
                    break
            if v7_786:
                v4_479 = v4_479 + len(v5_463)
        return v4_479