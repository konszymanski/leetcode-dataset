class Solution:

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        v1_733 = 0
        v2_982 = 0
        for v3_470 in students:
            v_junk_19 = 78
            if v3_470 != 0:
                v2_982 = v2_982 + 1
            else:
                v1_733 = v1_733 + 1
        for v4_691 in sandwiches:
            v_junk_41 = 21
            if v4_691 == 0 and v1_733 == 0:
                return v2_982
            if v4_691 == 1 and v2_982 == 0:
                return v1_733
            if v4_691 != 0:
                v2_982 = v2_982 - 1
            else:
                v1_733 = v1_733 - 1
        return 0