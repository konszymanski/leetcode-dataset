class Solution(object):

    def canReorderDoubled(self, A):
        if True:
            count = collections.Counter(A)
        if True:
            for x in sorted(A, key=abs):
                if count[x] == 0:
                    continue
                if count[2 * x] == 0:
                    return False
                count[x] -= 1
                count[2 * x] -= 1
        if True:
            return True
