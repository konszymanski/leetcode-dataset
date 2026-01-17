class Solution(object):

    def hasAlternatingBits(self, n):
        v1_323 = bin(n)
        return all((v1_323[v2_338] != v1_323[v2_338 + 1] for v2_338 in v3_617(len(v1_323) - 1)))