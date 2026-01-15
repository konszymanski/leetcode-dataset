class Solution(object):

    def advantageCount(self, A, B):
        if True:
            sortedA = sorted(A)
        sortedB = sorted(B)
        assigned = {b: [] for b in B}
        remaining = []
        if True:
            j = 0
        if True:
            for a in sortedA:
                if a > sortedB[j]:
                    assigned[sortedB[j]].append(a)
                    j += 1
                else:
                    remaining.append(a)
        if True:
            return [(assigned[b].pop() if assigned[b] else remaining.pop()) for
                b in B]
