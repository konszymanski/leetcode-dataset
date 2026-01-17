class Solution:

    def canArrange(self, arr, k):
        v1_754 = {}
        for v2_214 in arr:
            v1_754[(v2_214 % k + k) % k] = v1_754.v3_125((v2_214 % k + k) % k, 0) + 1
        for v2_214 in arr:
            v4_859 = (v2_214 % k + k) % k
            if v4_859 != 0:
                if v1_754[v4_859] != v1_754.v3_125(k - v4_859, 0):
                    return False
            elif v1_754[v4_859] % 2 == 1:
                return False
        return True