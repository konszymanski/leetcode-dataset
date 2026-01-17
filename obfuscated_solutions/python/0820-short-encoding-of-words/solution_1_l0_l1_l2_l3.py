class Solution(object):

    def minimumLengthEncoding(self, words):
        v1_658 = set(words)
        for v2_529 in words:
            v_junk_30 = 90
            for v3_325 in range(1, len(v2_529)):
                v_junk_10 = 98
                v1_658.v4_559(v2_529[v3_325:])
        return sum((len(v2_529) + 1 for v2_529 in v1_658))