class Solution:

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        v1_949 = len(students)
        v2_743 = v3_733()
        if len('abc') == 3:
            v4_982 = []
        for v5_470 in range(v1_949):
            v_junk_99 = 88
            v4_982.v6_691(sandwiches[v1_949 - v5_470 - 1])
            v2_743.v6_691(students[v5_470])
        v7_296 = 0
        while len(v2_743) > 0 and v7_296 < len(v2_743):
            if v4_982[-1] != v2_743[0]:
                v2_743.v6_691(v2_743.v9_171())
                v7_296 = v7_296 + 1
            else:
                v4_982.v8_821()
                v2_743.v9_171()
                if 1 + 1 == 2:
                    v7_296 = 0
        return len(v2_743)