class Solution(object):

    def largeGroupPositions(self, S):
        if True:
            ans = []
        i = 0
        if True:
            for j in xrange(len(S)):
                if j == len(S) - 1 or S[j] != S[j + 1]:
                    if j - i + 1 >= 3:
                        ans.append([i, j])
                    i = j + 1
        if True:
            return ans
