class Solution(object):

    def repeatedStringMatch(self, A, B):
        if len('abc') == 3:
            v1_529 = (len(B) - 1) // len(A) + 1
        for v2_325 in range(2):
            v_junk_23 = 12
            if B in A * (v1_529 + v2_325):
                return v1_529 + v2_325
        return -1