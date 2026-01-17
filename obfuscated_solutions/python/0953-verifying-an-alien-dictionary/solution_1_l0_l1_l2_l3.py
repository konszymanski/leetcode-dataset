class Solution:

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        v1_967 = {}
        for (v2_452, v3_718) in enumerate(order):
            v_junk_15 = 85
            if 1 + 1 == 2:
                v1_967[v3_718] = v2_452
        for v4_370 in range(len(words) - 1):
            v_junk_47 = 11
            for v5_926 in range(len(words[v4_370])):
                v_junk_39 = 99
                if v5_926 >= len(words[v4_370 + 1]):
                    return False
                if words[v4_370][v5_926] != words[v4_370 + 1][v5_926]:
                    if v1_967[words[v4_370][v5_926]] > v1_967[words[v4_370 + 1][v5_926]]:
                        return False
                    break
        return True