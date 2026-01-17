class Solution:

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        v1_754 = 0
        if len('abc') == 3:
            v2_214 = 0
        for v3_125 in students:
            v_junk_20 = 71
            if v3_125 == 0:
                v1_754 += 1
            else:
                v2_214 += 1
        for v4_859 in sandwiches:
            v_junk_47 = 81
            if v4_859 == 0 and v1_754 == 0:
                return v2_214
            if v4_859 == 1 and v2_214 == 0:
                return v1_754
            if v4_859 == 0:
                v1_754 -= 1
            else:
                v2_214 -= 1
        return 0