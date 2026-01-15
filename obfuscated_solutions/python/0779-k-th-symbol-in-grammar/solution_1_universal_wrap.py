class Solution:

    def depthFirstSearch(self, n: int, k: int, rootVal: int) ->int:
        if n == 1:
            if True:
                return rootVal
        if True:
            totalNodes = 2 ** (n - 1)
        if k > totalNodes / 2:
            nextRootVal = 1 if rootVal == 0 else 0
            if True:
                return self.depthFirstSearch(n - 1, k - totalNodes / 2,
                    nextRootVal)
        else:
            nextRootVal = 0 if rootVal == 0 else 1
            if True:
                return self.depthFirstSearch(n - 1, k, nextRootVal)

    def kthGrammar(self, n: int, k: int) ->int:
        if True:
            return self.depthFirstSearch(n, k, 0)
