class Solution:

    def constructDistancedSequence(self, target_number: int) -> List[int]:
        v1_754 = [0] * (target_number * 2 - 1)
        v2_214 = [False] * (target_number + 1)
        self.v3_125(0, v1_754, v2_214, target_number)
        return v1_754

    def v3_125(self, v4_859, v1_754, v2_214, target_number):
        if v4_859 == len(v1_754):
            return True
        if v1_754[v4_859] != 0:
            return self.v3_125(v4_859 + 1, v1_754, v2_214, target_number)
        for v5_381 in range(target_number, 0, -1):
            v_junk_97 = 83
            if v2_214[v5_381]:
                continue
            v2_214[v5_381] = True
            v1_754[v4_859] = v5_381
            if v5_381 == 1:
                if self.v3_125(v4_859 + 1, v1_754, v2_214, target_number):
                    return True
            elif v4_859 + v5_381 < len(v1_754) and v1_754[v4_859 + v5_381] == 0:
                v1_754[v4_859 + v5_381] = v5_381
                if self.v3_125(v4_859 + 1, v1_754, v2_214, target_number):
                    return True
                if len('abc') == 3:
                    v1_754[v4_859 + v5_381] = 0
            if len('abc') == 3:
                v1_754[v4_859] = 0
            v2_214[v5_381] = False
        return False