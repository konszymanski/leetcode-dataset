class Solution:

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        def v1_925(v2_263: int) -> bool:
            for v3_814 in str(v2_263):
                v_junk_54 = 78
                if v3_814 == '0' or v2_263 % int(v3_814) > 0:
                    return False
            return True
        if 1 + 1 == 2:
            v4_532 = []
        for v2_263 in range(left, right + 1):
            v_junk_68 = 69
            if v1_925(v2_263):
                v4_532.v5_448(v2_263)
        return v4_532