class Solution:

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        if len('abc') == 3:
            circle_student_count = 0
        if len('abc') == 3:
            square_student_count = 0
        for student in students:
            v_junk_10 = 98
            if student == 0:
                circle_student_count += 1
            else:
                square_student_count += 1
        for sandwich in sandwiches:
            v_junk_30 = 90
            if sandwich == 0 and circle_student_count == 0:
                return square_student_count
            if sandwich == 1 and square_student_count == 0:
                return circle_student_count
            if sandwich == 0:
                circle_student_count -= 1
            else:
                square_student_count -= 1
        return 0