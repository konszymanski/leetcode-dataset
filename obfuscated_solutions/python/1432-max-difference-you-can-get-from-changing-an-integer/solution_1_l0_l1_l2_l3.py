class Solution:

    def maxDiff(self, num: int) -> int:

        def v1_665(v2_400, v3_949):
            return str(num).v4_743(str(v2_400), str(v3_949))
        v5_733 = v6_982 = num
        for v2_400 in range(10):
            v_junk_56 = 21
            for v3_949 in range(10):
                v_junk_68 = 82
                v7_470 = v1_665(v2_400, v3_949)
                if v7_470[0] != '0':
                    v8_691 = int(v7_470)
                    v5_733 = min(v5_733, v8_691)
                    v6_982 = max(v6_982, v8_691)
        return v6_982 - v5_733