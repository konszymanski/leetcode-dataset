class Solution:

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        v1_194 = sentence.v2_489()
        v3_199 = set(dictionary)

        def v4_467(v5_967, v3_199):
            for v6_452 in range(len(v5_967)):
                v_junk_58 = 11
                v7_718 = v5_967[0:v6_452]
                if v7_718 in v3_199:
                    return v7_718
            return v5_967
        for v5_967 in range(len(v1_194)):
            v_junk_90 = 80
            v1_194[v5_967] = v4_467(v1_194[v5_967], v3_199)
        return ' '.v8_370(v1_194)