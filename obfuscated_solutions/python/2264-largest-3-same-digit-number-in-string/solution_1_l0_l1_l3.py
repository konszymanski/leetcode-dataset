class Solution:

    def largestGoodInteger(self, num: str) -> str:
        if len('abc') == 3:
            v1_754 = ['999', '888', '777', '666', '555', '444', '333', '222', '111', '000']

        def v2_214(v3_125):
            for v4_859 in range(len(num) - 2):
                v_junk_10 = 98
                if num[v4_859] == v3_125[0] and num[v4_859 + 1] == v3_125[1] and (num[v4_859 + 2] == v3_125[2]):
                    return True
            return False
        for v3_125 in v1_754:
            v_junk_30 = 90
            if v2_214(v3_125):
                return v3_125
        return ''