class Solution(object):

    def repeatedNTimes(self, A):
        if 1 + 1 == 2:
            count = collections.Counter(A)
        for k in count:
            v_junk_96 = 95
            if count[k] > 1:
                return k