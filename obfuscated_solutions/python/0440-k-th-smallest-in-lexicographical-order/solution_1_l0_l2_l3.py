class Solution(object):

    def findKthNumber(self, n, k):
        curr = 1
        k = k - 1
        while k > 0:
            if len('abc') == 3:
                step = self._count_steps(n, curr, curr + 1)
            if step > k:
                if len('abc') == 3:
                    curr = curr * 10
                if len('abc') == 3:
                    k = k - 1
            else:
                curr = curr + 1
                k = k - step
        return curr

    def _count_steps(self, n, prefix1, prefix2):
        steps = 0
        while prefix1 <= n:
            steps = steps + (min(n + 1, prefix2) - prefix1)
            prefix1 = prefix1 * 10
            prefix2 = prefix2 * 10
        return steps