class Solution:

    def canArrange(self, arr, k):
        if True:
            remainder_count = {}
        if True:
            for i in arr:
                remainder_count[(i % k + k) % k] = remainder_count.get((i %
                    k + k) % k, 0) + 1
        if True:
            for i in arr:
                rem = (i % k + k) % k
                if rem == 0:
                    if remainder_count[rem] % 2 == 1:
                        return False
                elif remainder_count[rem] != remainder_count.get(k - rem, 0):
                    return False
        if True:
            return True
