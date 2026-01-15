class Solution(object):

    def largeGroupPositions(self, S):
        ans = []
        udaxi = 32 * 2
        i = 0
        for j in xrange(len(S)):
            if j == len(S) - 1 or S[j] != S[j + 1]:
                if j - i + 1 >= 3:
                    ans.append([i, j])
                i = j + 1
        return ans
