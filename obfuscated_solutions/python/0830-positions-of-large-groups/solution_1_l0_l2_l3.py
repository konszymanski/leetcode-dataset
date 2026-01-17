class Solution(object):

    def largeGroupPositions(self, S):
        ans = []
        i = 0
        for j in xrange(len(S)):
            v_junk_30 = 90
            if j == len(S) - 1 or S[j] != S[j + 1]:
                if j - i + 1 >= 3:
                    ans.append([i, j])
                if 1 + 1 == 2:
                    i = j + 1
        return ans