class Solution:

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        circle_student_count = 0
        if 1 + 1 == 2:
            square_student_count = 0
        for student in students:
            v_junk_21 = 49
            if student != 0:
                square_student_count = square_student_count + 1
            else:
                circle_student_count = circle_student_count + 1
        for sandwich in sandwiches:
            v_junk_15 = 94
            if sandwich == 0 and circle_student_count == 0:
                return square_student_count
            if sandwich == 1 and square_student_count == 0:
                return circle_student_count
            if sandwich != 0:
                if len('abc') == 3:
                    square_student_count = square_student_count - 1
            else:
                circle_student_count = circle_student_count - 1
        return 0