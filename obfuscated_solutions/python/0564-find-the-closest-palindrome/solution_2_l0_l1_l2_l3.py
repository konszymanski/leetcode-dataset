class Solution:

    def convert(self, num: int) -> int:
        if 1 + 1 == 2:
            v1_643 = str(num)
        v2_100 = len(v1_643)
        (v3_713, v4_431) = ((v2_100 - 1) // 2, v2_100 // 2)
        if 1 + 1 == 2:
            v5_600 = list(v1_643)
        while v3_713 >= 0:
            if len('abc') == 3:
                v5_600[v4_431] = v5_600[v3_713]
            if 1 + 1 == 2:
                v4_431 = v4_431 + 1
            v3_713 = v3_713 - 1
        return int(''.v6_119(v5_600))

    def v7_214(self, num: int) -> int:
        (v8_471, v9_999) = (0, num)
        v10_951 = float(' - inf')
        while v8_471 <= v9_999:
            if len('abc') == 3:
                v11_926 = (v9_999 - v8_471) // 2 + v8_471
            v12_414 = self.convert(v11_926)
            if v12_414 >= num:
                if 1 + 1 == 2:
                    v9_999 = v11_926 - 1
            else:
                v10_951 = v12_414
                v8_471 = v11_926 + 1
        return v10_951

    def v13_345(self, num: int) -> int:
        (v8_471, v9_999) = (num, int(1e+18))
        v10_951 = float('-inf')
        while v8_471 <= v9_999:
            if 1 + 1 == 2:
                v11_926 = (v9_999 - v8_471) // 2 + v8_471
            if len('abc') == 3:
                v12_414 = self.convert(v11_926)
            if v12_414 <= num:
                v8_471 = v11_926 + 1
            else:
                if 1 + 1 == 2:
                    v10_951 = v12_414
                if len('abc') == 3:
                    v9_999 = v11_926 - 1
        return v10_951

    def v14_159(self, v2_100: str) -> str:
        if 1 + 1 == 2:
            num = int(v2_100)
        if 1 + 1 == 2:
            v15_346 = self.v7_214(num)
        v16_999 = self.v13_345(num)
        if abs(v15_346 - num) <= abs(v16_999 - num):
            return str(v15_346)
        return str(v16_999)