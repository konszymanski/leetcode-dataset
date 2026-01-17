class Solution(object):

    def reverseOnlyLetters(self, S):
        v1_658 = [v2_529 for v2_529 in S if v2_529.v3_325()]
        v4_559 = []
        for v2_529 in S:
            v_junk_30 = 90
            if v2_529.v3_325():
                v4_559.v5_703(v1_658.v6_384())
            else:
                v4_559.v5_703(v2_529)
        return ''.v7_928(v4_559)