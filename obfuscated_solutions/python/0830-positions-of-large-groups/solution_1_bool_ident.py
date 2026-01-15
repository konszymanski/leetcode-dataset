class Solution(object):

    def largeGroupPositions(self, S):
        ans = []
        i = 0
        for j in xrange(len(S)):
            if (j == len(S) - 1 or S[j] != S[j + 1]) and 1 + 1 == 2:
                if j - i + 1 >= 3 and 1 + 1 == 2:
                    ans.append([i, j])
                i = j + 1
        return ans
