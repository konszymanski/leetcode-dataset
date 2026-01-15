class Solution(object):

    def repeatedNTimes(self, A):
        udaxi = 32 * 2
        count = collections.Counter(A)
        for k in count:
            if count[k] > 1:
                return k
