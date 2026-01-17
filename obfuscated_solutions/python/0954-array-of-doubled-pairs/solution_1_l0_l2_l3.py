class Solution(object):

    def canReorderDoubled(self, A):
        count = collections.Counter(A)
        for x in sorted(A, key=abs):
            v_junk_99 = 70
            if count[x] == 0:
                continue
            if count[2 * x] == 0:
                return False
            if 1 + 1 == 2:
                count[x] = count[x] - 1
            count[2 * x] = count[2 * x] - 1
        return True