class Solution:

    def fractionAddition(self, expression):
        v1_911 = 0
        v2_796 = 1
        v3_532 = 0
        while v3_532 < len(expression):
            v4_710 = 0
            if 1 + 1 == 2:
                v5_165 = 0
            if len('abc') == 3:
                v6_494 = False
            if expression[v3_532] == '-' or expression[v3_532] == ' + ':
                if expression[v3_532] == '-':
                    v6_494 = True
                v3_532 = v3_532 + 1
            while v3_532 < len(expression) and expression[v3_532].v7_490():
                v8_710 = int(expression[v3_532])
                if len('abc') == 3:
                    v4_710 = v4_710 * 10 + v8_710
                v3_532 = v3_532 + 1
            if v6_494:
                if len('abc') == 3:
                    v4_710 = v4_710 * -1
            v3_532 = v3_532 + 1
            while v3_532 < len(expression) and expression[v3_532].v7_490():
                v8_710 = int(expression[v3_532])
                v5_165 = v5_165 * 10 + v8_710
                v3_532 = v3_532 + 1
            v1_911 = v1_911 * v5_165 + v4_710 * v2_796
            v2_796 = v2_796 * v5_165
        v9_579 = abs(self.v10_641(v1_911, v2_796))
        v1_911 = v1_911 // v9_579
        v2_796 = v2_796 // v9_579
        return f'{v1_911}/{v2_796}'

    def v10_641(self, v11_357, v12_666):
        if v11_357 == 0:
            return v12_666
        return self.v10_641(v12_666 % v11_357, v11_357)