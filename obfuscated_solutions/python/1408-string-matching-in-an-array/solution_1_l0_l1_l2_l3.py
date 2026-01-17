class Solution:

    def stringMatching(self, words):
        v1_658 = []
        for v2_529 in range(len(words)):
            v_junk_30 = 90
            for v3_325 in range(len(words)):
                v_junk_10 = 98
                if v2_529 == v3_325:
                    continue
                if words[v2_529] in words[v3_325]:
                    v1_658.v4_559(words[v2_529])
                    break
        return v1_658