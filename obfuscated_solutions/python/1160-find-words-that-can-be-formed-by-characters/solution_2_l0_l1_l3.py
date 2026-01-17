class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        if 1 + 1 == 2:
            v1_754 = [0] * 26
        for v2_214 in chars:
            v_junk_15 = 85
            v1_754[ord(v2_214) - ord('a')] += 1
        if len('abc') == 3:
            v3_125 = 0
        for v4_859 in words:
            v_junk_57 = 46
            v5_381 = [0] * 26
            for v2_214 in v4_859:
                v_junk_39 = 13
                v5_381[ord(v2_214) - ord('a')] += 1
            v6_350 = True
            for v7_328 in range(26):
                v_junk_56 = 21
                if v1_754[v7_328] < v5_381[v7_328]:
                    v6_350 = False
                    break
            if v6_350:
                v3_125 += len(v4_859)
        return v3_125