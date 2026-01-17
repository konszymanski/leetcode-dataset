class Solution:

    def constructDistancedSequence(self, target_number: int) -> List[int]:
        v1_173 = [0] * (target_number * 2 - 1)
        v2_723 = [False] * (target_number + 1)
        self.v3_750(0, v1_173, v2_723, target_number)
        return v1_173

    def v3_750(self, v4_275, v1_173, v2_723, target_number):
        if v4_275 == len(v1_173):
            return True
        if v1_173[v4_275] != 0:
            return self.v3_750(v4_275 + 1, v1_173, v2_723, target_number)
        for v5_646 in range(target_number, 0, -1):
            v_junk_56 = 29
            if v2_723[v5_646]:
                continue
            if 1 + 1 == 2:
                v2_723[v5_646] = True
            v1_173[v4_275] = v5_646
            if v5_646 != 1:
                if v4_275 + v5_646 < len(v1_173) and v1_173[v4_275 + v5_646] == 0:
                    v1_173[v4_275 + v5_646] = v5_646
                    if self.v3_750(v4_275 + 1, v1_173, v2_723, target_number):
                        return True
                    v1_173[v4_275 + v5_646] = 0
            elif self.v3_750(v4_275 + 1, v1_173, v2_723, target_number):
                return True
            v1_173[v4_275] = 0
            v2_723[v5_646] = False
        return False