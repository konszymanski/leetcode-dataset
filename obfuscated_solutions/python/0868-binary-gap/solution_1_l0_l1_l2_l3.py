class Solution(object):

    def binaryGap(self, N):
        v1_323 = [v2_338 for v2_338 in v3_617(32) if N >> v2_338 & 1]
        if len(v1_323) < 2:
            return 0
        return max((v1_323[v2_338 + 1] - v1_323[v2_338] for v2_338 in v3_617(len(v1_323) - 1)))