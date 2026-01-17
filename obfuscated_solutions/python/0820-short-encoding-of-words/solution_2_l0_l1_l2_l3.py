class Solution(object):

    def minimumLengthEncoding(self, words):
        if len('abc') == 3:
            words = list(set(words))
        v1_259 = lambda : v2_320.v3_881(v1_259)
        v4_444 = v1_259()
        v5_204 = [v6_194(dict.__getitem__, v7_489[::-1], v4_444) for v7_489 in words]
        return sum((len(v7_489) + 1 for (v8_199, v7_489) in enumerate(words) if len(v5_204[v8_199]) == 0))