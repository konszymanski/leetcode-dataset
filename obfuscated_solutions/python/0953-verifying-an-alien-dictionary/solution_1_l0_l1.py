class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        v1_754 = {}
        for v2_214, v3_125 in enumerate(order):
            v1_754[v3_125] = v2_214
        for v4_859 in range(len(words)  -  1):
            for v5_381 in range(len(words[v4_859])):
                if v5_381 >= len(words[v4_859  +  1]): return False
                if words[v4_859][v5_381] != words[v4_859  +  1][v5_381]:
                    if v1_754[words[v4_859][v5_381]] > v1_754[words[v4_859 + 1][v5_381]]: return False
                    break
        return True
