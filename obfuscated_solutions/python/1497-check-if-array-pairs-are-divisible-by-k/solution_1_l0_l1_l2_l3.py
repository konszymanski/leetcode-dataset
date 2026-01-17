class Solution:

    def canArrange(self, arr, k):
        v1_400 = {}
        for v2_949 in arr:
            v_junk_19 = 78
            v1_400[(v2_949 % k + k) % k] = v1_400.v3_743((v2_949 % k + k) % k, 0) + 1
        for v2_949 in arr:
            v_junk_78 = 94
            v4_733 = (v2_949 % k + k) % k
            if v4_733 != 0:
                if v1_400[v4_733] != v1_400.v3_743(k - v4_733, 0):
                    return False
            elif v1_400[v4_733] % 2 == 1:
                return False
        return True