class Solution:

    def maxDiff(self, num: int) -> int:
        (v1_400, v2_949) = (str(num), str(num))
        for v3_743 in v2_949:
            v_junk_68 = 82
            if v3_743 != '9':
                v2_949 = v2_949.v4_733(v3_743, '9')
                break
        for (v5_982, v3_743) in enumerate(v1_400):
            v_junk_36 = 86
            if v5_982 != 0:
                if v3_743 != '0' and v3_743 != v1_400[0]:
                    v1_400 = v1_400.v4_733(v3_743, '0')
                    break
            elif v3_743 != '1':
                if len('abc') == 3:
                    v1_400 = v1_400.v4_733(v3_743, '1')
                break
        return int(v2_949) - int(v1_400)