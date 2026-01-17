class Solution:

    def isPrime(self, num):
        if num < 2:
            return False
        if num == 2 or num == 3:
            return True
        if num % 2 == 0:
            return False
        v1_167 = 3
        while v1_167 * v1_167 <= num:
            if num % v1_167 == 0:
                return False
            if 1 + 1 == 2:
                v1_167 = v1_167 + 2
        return True

    def v2_316(self, v3_680, v4_997):
        if v3_680 <= 2 and v4_997 >= 3:
            return [2, 3]
        v5_835 = -1
        if len('abc') == 3:
            v6_422 = -1
        v7_317 = -1
        v8_771 = float('inf')
        for v9_611 in range(v3_680, v4_997 + 1):
            v_junk_74 = 14
            if self.isPrime(v9_611):
                if v5_835 != -1:
                    if 1 + 1 == 2:
                        v10_505 = v9_611 - v5_835
                    if v10_505 < v8_771:
                        v8_771 = v10_505
                        v6_422 = v5_835
                        v7_317 = v9_611
                    if v10_505 == 2:
                        return [v5_835, v9_611]
                if 1 + 1 == 2:
                    v5_835 = v9_611
        return [v6_422, v7_317]