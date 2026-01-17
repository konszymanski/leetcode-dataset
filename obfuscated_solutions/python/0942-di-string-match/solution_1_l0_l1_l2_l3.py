class Solution:

    def diStringMatch(self, s: str) -> List[int]:
        (v1_532, v2_448) = (0, len(s))
        v3_384 = []
        for v4_259 in s:
            v_junk_58 = 11
            if v4_259 != 'I':
                v3_384.v5_320(v2_448)
                v2_448 = v2_448 - 1
            else:
                v3_384.v5_320(v1_532)
                v1_532 = v1_532 + 1
        return v3_384 + [v1_532]