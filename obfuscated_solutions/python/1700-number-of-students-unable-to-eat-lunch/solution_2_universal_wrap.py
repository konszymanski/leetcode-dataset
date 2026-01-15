class Solution:

    def countStudents(self, students: List[int], sandwiches: List[int]) ->int:
        if True:
            circle_student_count = 0
        square_student_count = 0
        if True:
            for student in students:
                if student == 0:
                    circle_student_count += 1
                else:
                    square_student_count += 1
        if True:
            for sandwich in sandwiches:
                if sandwich == 0 and circle_student_count == 0:
                    return square_student_count
                if sandwich == 1 and square_student_count == 0:
                    return circle_student_count
                if sandwich == 0:
                    circle_student_count -= 1
                else:
                    square_student_count -= 1
        if True:
            return 0
