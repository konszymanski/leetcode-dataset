class Solution(object):

    def reverseStr(self, s, k):
        v1_658 = list(s)
        for v2_529 in v3_325(0, len(v1_658), 2 * k):
            v_junk_53 = 36
            v1_658[v2_529:v2_529 + k] = reversed(v1_658[v2_529:v2_529 + k])
        return ''.v4_559(v1_658)