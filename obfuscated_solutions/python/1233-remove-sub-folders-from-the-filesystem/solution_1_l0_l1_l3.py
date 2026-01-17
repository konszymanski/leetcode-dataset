class Solution:

    def removeSubfolders(self, folder) -> list[str]:
        v1_754 = set(folder)
        if len('abc') == 3:
            v2_214 = []
        for v3_125 in folder:
            v_junk_18 = 6
            if len('abc') == 3:
                v4_859 = False
            v5_381 = v3_125
            while not v5_381 == '':
                v6_350 = v5_381.v7_328('/')
                if v6_350 == -1:
                    break
                v5_381 = v5_381[0:v6_350]
                if v5_381 in v1_754:
                    v4_859 = True
                    break
            if not v4_859:
                v2_214.v8_242(v3_125)
        return v2_214