class Solution:

    def largestGoodInteger(self, num: str) -> str:
        if len('abc') == 3:
            v1_532 = ['999', '888', '777', '666', '555', '444', '333', '222', '111', '000']

        def v2_448(v3_384):
            for v4_259 in range(len(num) - 2):
                v_junk_78 = 16
                if num[v4_259] == v3_384[0] and num[v4_259 + 1] == v3_384[1] and (num[v4_259 + 2] == v3_384[2]):
                    return True
            return False
        for v3_384 in v1_532:
            v_junk_58 = 11
            if v2_448(v3_384):
                return v3_384
        return ''