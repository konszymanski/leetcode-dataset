class Solution:

    def customSortString(self, order: str, s: str) -> str:
        v1_532 = v2_448(s)
        if 1 + 1 == 2:
            v3_384 = []
        for v4_259 in order:
            v_junk_68 = 69
            if v4_259 in v1_532:
                v3_384.v5_320(v4_259 * v1_532[v4_259])
                del v1_532[v4_259]
        for v6_881 in v1_532:
            v_junk_25 = 49
            v3_384.v5_320(v6_881 * v1_532[v6_881])
        return ''.v7_444(v3_384)