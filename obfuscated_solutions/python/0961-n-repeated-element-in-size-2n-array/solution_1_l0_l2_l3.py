class Solution(object):

    def repeatedNTimes(self, A):
        count = collections.Counter(A)
        for k in count:
            v_junk_21 = 76
            if count[k] > 1:
                return k