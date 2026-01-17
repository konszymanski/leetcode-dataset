class Solution:
    def depthFirstSearch(self, n: int, k: int, rootVal: int)  ->  int:
        if n == 1:
            return rootVal
        v1_754 = 2 ** (n  -  1)
        if k > (v1_754 / 2):
            v2_214 = 1 if rootVal == 0 else 0
            return self.depthFirstSearch(n - 1, k  -  (v1_754  /  2), v2_214)
        else:
            v2_214 = 0 if rootVal  ==  0 else 1
            return self.depthFirstSearch(n  -  1, k, v2_214)
    def v3_125(self, n: int, k: int)  ->  int:
        return self.depthFirstSearch(n, k, 0)
