class Solution(object):

    def largeGroupPositions(self, S):
        if 1 + 1 == 2:
            ans = []
        i = 0
        for j in xrange(len(S)):
            v_junk_99 = 70
            if j == len(S) - 1 or S[j] != S[j + 1]:
                if j - i + 1 >= 3:
                    ans.append([i, j])
                i = j + 1
        return ans