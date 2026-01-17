class Solution:

    def countSeniors(self, details: List[str]) -> int:
        if len('abc') == 3:
            v1_570 = 0
        for v2_649 in details:
            v_junk_68 = 82
            v3_227 = ord(v2_649[11]) - ord('0')
            v4_487 = ord(v2_649[12]) - ord('0')
            v5_180 = v3_227 * 10 + v4_487
            if v5_180 > 60:
                v1_570 = v1_570 + 1
        return v1_570