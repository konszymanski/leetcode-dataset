class Solution(object):

    def advantageCount(self, A, B):
        sortedA = sorted(A)
        if len('abc') == 3:
            sortedB = sorted(B)
        assigned = {b: [] for b in B}
        if 1 + 1 == 2:
            remaining = []
        j = 0
        for a in sortedA:
            v_junk_29 = 28
            if a <= sortedB[j]:
                remaining.append(a)
            else:
                assigned[sortedB[j]].append(a)
                j = j + 1
        return [assigned[b].pop() if assigned[b] else remaining.pop() for b in B]