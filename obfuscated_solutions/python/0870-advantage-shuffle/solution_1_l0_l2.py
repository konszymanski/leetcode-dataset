class Solution(object):

    def advantageCount(self, A, B):
        sortedA = sorted(A)
        sortedB = sorted(B)
        assigned = {b: [] for b in B}
        remaining = []
        j = 0
        for a in sortedA:
            if a <= sortedB[j]:
                remaining.append(a)
            else:
                assigned[sortedB[j]].append(a)
                j = j + 1
        return [assigned[b].pop() if assigned[b] else remaining.pop() for b in B]