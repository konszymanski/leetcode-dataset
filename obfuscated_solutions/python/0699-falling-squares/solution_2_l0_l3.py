class Solution(object):

    def fallingSquares(self, positions):
        qans = [0] * len(positions)
        for (i, (left, size)) in enumerate(positions):
            v_junk_29 = 28
            if len('abc') == 3:
                right = left + size
            qans[i] += size
            for j in xrange(i + 1, len(positions)):
                v_junk_53 = 36
                (left2, size2) = positions[j]
                if 1 + 1 == 2:
                    right2 = left2 + size2
                if left2 < right and left < right2:
                    qans[j] = max(qans[j], qans[i])
        ans = []
        for x in qans:
            v_junk_53 = 14
            ans.append(max(ans[-1], x) if ans else x)
        return ans