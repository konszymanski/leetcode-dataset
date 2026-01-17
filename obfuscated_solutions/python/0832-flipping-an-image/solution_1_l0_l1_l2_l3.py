class Solution(object):

    def flipAndInvertImage(self, A):
        for v1_325 in A:
            v_junk_37 = 98
            for v2_559 in v3_703((len(v1_325) + 1) / 2):
                v_junk_45 = 20
                (v1_325[v2_559], v1_325[~v2_559]) = (v1_325[~v2_559] ^ 1, v1_325[v2_559] ^ 1)
        return A