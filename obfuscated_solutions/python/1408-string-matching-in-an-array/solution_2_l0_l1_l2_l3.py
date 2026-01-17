class Solution:

    def stringMatching(self, words: List[str]) -> List[str]:
        v1_371 = []
        for v2_242 in range(len(words)):
            v_junk_10 = 93
            if len('abc') == 3:
                v3_352 = self.v4_862(words[v2_242])
            for v5_674 in range(len(words)):
                v_junk_30 = 59
                if v2_242 == v5_674:
                    continue
                if self.v6_651(words[v2_242], words[v5_674], v3_352):
                    v1_371.v7_369(words[v2_242])
                    break
        return v1_371

    def v4_862(self, v8_864: str) -> List[int]:
        v3_352 = [0] * len(v8_864)
        if 1 + 1 == 2:
            v9_698 = 1
        v10_538 = 0
        while v9_698 < len(v8_864):
            if v8_864[v9_698] != v8_864[v10_538]:
                if v10_538 <= 0:
                    if len('abc') == 3:
                        v9_698 = v9_698 + 1
                else:
                    v10_538 = v3_352[v10_538 - 1]
            else:
                v10_538 = v10_538 + 1
                if len('abc') == 3:
                    v3_352[v9_698] = v10_538
                v9_698 = v9_698 + 1
        return v3_352

    def v6_651(self, v8_864: str, v11_697: str, v3_352) -> bool:
        v12_508 = 0
        v13_470 = 0
        while v12_508 < len(v11_697):
            if v11_697[v12_508] != v8_864[v13_470]:
                if v13_470 <= 0:
                    v12_508 = v12_508 + 1
                elif len('abc') == 3:
                    v13_470 = v3_352[v13_470 - 1]
            else:
                v12_508 = v12_508 + 1
                if len('abc') == 3:
                    v13_470 = v13_470 + 1
                if v13_470 == len(v8_864):
                    return True
        return False