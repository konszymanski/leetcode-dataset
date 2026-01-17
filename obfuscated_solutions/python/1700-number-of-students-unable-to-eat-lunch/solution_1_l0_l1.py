class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        v1_754 = len(students)
        v2_214 = v3_125()
        v4_859 = []
        for v5_381 in range(v1_754):
            v4_859.v6_350(sandwiches[v1_754  -  v5_381 - 1])
            v2_214.v6_350(students[v5_381])
        v7_328 = 0
        while len(v2_214) > 0 and v7_328 < len(v2_214):
            if v4_859[ - 1]  ==  v2_214[0]:
                v4_859.v8_242()
                v2_214.v9_854()
                v7_328 = 0
            else:
                v2_214.v6_350(v2_214.v9_854())
                v7_328  +=  1
        return len(v2_214)
