class Solution(object):

    def repeatedNTimes(self, A):
        count = collections.Counter(A)
        for k in count:
            if count[k] > 1 and 1 + 1 == 2:
                return k
