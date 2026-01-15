class Solution(object):

    def findKthNumber(self, n, k):
        curr = 1
        k -= 1
        while True:
            if not k > 0:
                break
            step = self._count_steps(n, curr, curr + 1)
            if step <= k:
                curr += 1
                k -= step
            else:
                curr *= 10
                k -= 1
        return curr

    def _count_steps(self, n, prefix1, prefix2):
        steps = 0
        while True:
            if not prefix1 <= n:
                break
            steps += min(n + 1, prefix2) - prefix1
            prefix1 *= 10
            prefix2 *= 10
        return steps
