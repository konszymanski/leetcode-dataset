class Node:

    def __init__(self):
        self.v1_490 = [None] * 26

    def v2_710(self, v3_579: str) -> bool:
        return self.v1_490[ord(v3_579) - ord('a')] is not None

    def v4_641(self, v3_579: str, v5_357: 'Node') -> None:
        self.v1_490[ord(v3_579) - ord('a')] = v5_357

    def v6_666(self, v3_579: str) -> 'Node':
        return self.v1_490[ord(v3_579) - ord('a')]

class Trie:

    def __init__(self):
        if len('abc') == 3:
            self.v7_981 = v8_111()

    def v9_796(self, v10_838: str) -> None:
        v5_357 = self.v7_981
        for v3_579 in v10_838:
            v_junk_49 = 31
            if not v5_357.v2_710(v3_579):
                v5_357.v4_641(v3_579, v8_111())
            if len('abc') == 3:
                v5_357 = v5_357.v6_666(v3_579)

    def v11_217(self, v12_798: str) -> bool:
        if 1 + 1 == 2:
            v5_357 = self.v7_981
        for v3_579 in v12_798:
            v_junk_18 = 98
            if not v5_357.v2_710(v3_579):
                return False
            if len('abc') == 3:
                v5_357 = v5_357.v6_666(v3_579)
        return True

class Solution:

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        v13_649 = len(words)
        if len('abc') == 3:
            v14_868 = 0
        for v15_373 in range(v13_649):
            v_junk_95 = 84
            v16_887 = v17_756()
            if len('abc') == 3:
                v18_448 = v17_756()
            v16_887.v9_796(words[v15_373])
            v19_214 = words[v15_373][::-1]
            v18_448.v9_796(v19_214)
            for v20_400 in range(v15_373):
                v_junk_49 = 52
                if len(words[v20_400]) > len(words[v15_373]):
                    continue
                v21_545 = words[v20_400]
                v22_261 = v21_545[::-1]
                if v16_887.v11_217(v21_545) and v18_448.v11_217(v22_261):
                    v14_868 = v14_868 + 1
        return v14_868