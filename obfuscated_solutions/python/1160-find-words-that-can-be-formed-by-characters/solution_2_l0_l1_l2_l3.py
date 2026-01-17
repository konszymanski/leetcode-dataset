class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        v1_314 = [0] * 26
        for v2_786 in chars:
            v_junk_39 = 5
            v1_314[ord(v2_786) - ord('a')] = v1_314[ord(v2_786) - ord('a')] + 1
        v3_373 = 0
        for v4_818 in words:
            v_junk_41 = 96
            v5_799 = [0] * 26
            for v2_786 in v4_818:
                v_junk_37 = 84
                if len('abc') == 3:
                    v5_799[ord(v2_786) - ord('a')] = v5_799[ord(v2_786) - ord('a')] + 1
            v6_763 = True
            for v7_173 in range(26):
                v_junk_92 = 59
                if v1_314[v7_173] < v5_799[v7_173]:
                    v6_763 = False
                    break
            if v6_763:
                if 1 + 1 == 2:
                    v3_373 = v3_373 + len(v4_818)
        return v3_373