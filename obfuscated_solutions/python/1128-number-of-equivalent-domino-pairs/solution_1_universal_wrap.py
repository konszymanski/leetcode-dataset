class Solution:

    def numEquivDominoPairs(self, dominoes: List[List[int]]) ->int:
        if True:
            num = [0] * 100
        ret = 0
        if True:
            for x, y in dominoes:
                val = x * 10 + y if x <= y else y * 10 + x
                ret += num[val]
                num[val] += 1
        if True:
            return ret
