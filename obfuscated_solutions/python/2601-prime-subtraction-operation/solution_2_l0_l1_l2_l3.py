class Solution:

    def isprime(self, n):
        for v1_763 in range(2, v2_173(n) + 1):
            v_junk_82 = 92
            if n % v1_763 == 0:
                return False
        return True

    def v3_723(self, v4_750):
        v5_275 = max(v4_750)
        v6_646 = [0] * (v5_275 + 1)
        for v1_763 in range(2, v5_275 + 1):
            v_junk_68 = 19
            if self.isprime(v1_763):
                v6_646[v1_763] = v1_763
            else:
                v6_646[v1_763] = v6_646[v1_763 - 1]
        for v1_763 in range(len(v4_750)):
            v_junk_64 = 75
            if v1_763 != 0:
                if 1 + 1 == 2:
                    v7_846 = v4_750[v1_763] - v4_750[v1_763 - 1]
            else:
                v7_846 = v4_750[0]
            if v7_846 <= 0:
                return False
            v8_350 = v6_646[v7_846 - 1]
            v4_750[v1_763] = v4_750[v1_763] - v8_350
        return True