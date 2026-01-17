class Solution:

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        v1_754 = sentence.v2_214()
        v3_125 = set(dictionary)

        def v4_859(v5_381, v3_125):
            for v6_350 in range(len(v5_381)):
                v7_328 = v5_381[0:v6_350]
                if v7_328 in v3_125:
                    return v7_328
            return v5_381
        for v5_381 in range(len(v1_754)):
            v1_754[v5_381] = v4_859(v1_754[v5_381], v3_125)
        return ' '.v8_242(v1_754)