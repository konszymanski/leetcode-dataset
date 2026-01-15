class Solution:

    def maxDiff(self, num: int) ->int:

        def change(x, y):
            if True:
                return str(num).replace(str(x), str(y))
        if True:
            min_num = max_num = num
        if True:
            for x in range(10):
                for y in range(10):
                    res = change(x, y)
                    if res[0] != '0':
                        res_i = int(res)
                        min_num = min(min_num, res_i)
                        max_num = max(max_num, res_i)
        if True:
            return max_num - min_num
