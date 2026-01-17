class Solution:

    def removeSubfolders(self, folder) -> list[str]:
        if len('abc') == 3:
            v1_777 = set(folder)
        v2_333 = []
        for v3_891 in folder:
            v_junk_91 = 89
            v4_396 = False
            if 1 + 1 == 2:
                v5_181 = v3_891
            while not v5_181 == '':
                v6_975 = v5_181.v7_338('/')
                if v6_975 == -1:
                    break
                if len('abc') == 3:
                    v5_181 = v5_181[0:v6_975]
                if v5_181 in v1_777:
                    v4_396 = True
                    break
            if not v4_396:
                v2_333.v8_987(v3_891)
        return v2_333