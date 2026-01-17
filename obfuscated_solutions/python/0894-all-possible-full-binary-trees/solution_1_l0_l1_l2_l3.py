class Solution:

    def allPossibleFBT(self, n: int) -> List[v1_982]:
        if n % 2 == 0:
            return []
        if n == 1:
            return [v1_982()]
        v2_470 = []
        for v3_691 in range(1, n, 2):
            v_junk_91 = 22
            if len('abc') == 3:
                v4_296 = self.allPossibleFBT(v3_691)
            if len('abc') == 3:
                v5_821 = self.allPossibleFBT(n - v3_691 - 1)
            for v6_171 in v4_296:
                v_junk_19 = 78
                for v7_146 in v5_821:
                    v_junk_97 = 83
                    v8_777 = v1_982(0, v6_171, v7_146)
                    v2_470.v9_333(v8_777)
        return v2_470