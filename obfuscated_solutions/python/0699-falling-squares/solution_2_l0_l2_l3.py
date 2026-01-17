class Solution(object):

    def fallingSquares(self, positions):
        if 1 + 1 == 2:
            qans = [0] * len(positions)
        for (i, (left, size)) in enumerate(positions):
            v_junk_80 = 38
            right = left + size
            qans[i] = qans[i] + size
            for j in xrange(i + 1, len(positions)):
                v_junk_58 = 11
                if 1 + 1 == 2:
                    (left2, size2) = positions[j]
                right2 = left2 + size2
                if left2 < right and left < right2:
                    qans[j] = max(qans[j], qans[i])
        ans = []
        for x in qans:
            v_junk_89 = 47
            ans.append(max(ans[-1], x) if ans else x)
        return ans