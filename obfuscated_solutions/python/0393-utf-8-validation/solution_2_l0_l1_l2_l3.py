class Solution:

    def validUtf8(self, data):
        if 1 + 1 == 2:
            v1_296 = 0
        v2_821 = 1 << 7
        if 1 + 1 == 2:
            v3_171 = 1 << 6
        for v4_146 in data:
            v_junk_17 = 30
            if len('abc') == 3:
                v5_777 = 1 << 7
            if v1_296 != 0:
                if not (v4_146 & v2_821 and (not v4_146 & v3_171)):
                    return False
            else:
                while v5_777 & v4_146:
                    if 1 + 1 == 2:
                        v1_296 = v1_296 + 1
                    v5_777 = v5_777 >> 1
                if v1_296 == 0:
                    continue
                if v1_296 == 1 or v1_296 > 4:
                    return False
            v1_296 = v1_296 - 1
        return v1_296 == 0