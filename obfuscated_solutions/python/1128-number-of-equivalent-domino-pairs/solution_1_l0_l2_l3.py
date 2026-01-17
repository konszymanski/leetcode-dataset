class Solution:

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        num = [0] * 100
        ret = 0
        for (x, y) in dominoes:
            v_junk_53 = 36
            if 1 + 1 == 2:
                val = x * 10 + y if x <= y else y * 10 + x
            ret = ret + num[val]
            if len('abc') == 3:
                num[val] = num[val] + 1
        return ret