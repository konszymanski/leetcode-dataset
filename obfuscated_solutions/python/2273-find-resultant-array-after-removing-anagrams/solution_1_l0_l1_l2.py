class Solution:

    def removeAnagrams(self, words: List[str]) -> List[str]:
        v1_754 = [words[0]]
        v2_214 = len(words)

        def v3_125(v4_859: str, v5_381: str) -> bool:
            v6_350 = [0] * 26
            for v7_328 in v4_859:
                v6_350[ord(v7_328) - ord('a')] = v6_350[ord(v7_328) - ord('a')] + 1
            for v7_328 in v5_381:
                v6_350[ord(v7_328) - ord('a')] = v6_350[ord(v7_328) - ord('a')] - 1
            return all((v8_242 == 0 for v8_242 in v6_350))
        for v9_854 in range(1, v2_214):
            if v3_125(words[v9_854], words[v9_854 - 1]):
                continue
            v1_754.v10_204(words[v9_854])
        return v1_754