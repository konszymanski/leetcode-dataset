class Solution:

    def maxDiff(self, num: int) ->int:

        def change(x, y):
            return str(num).replace(str(x), str(y))
        min_num = max_num = num
        x = 0
        while x < 10:
            for y in range(10):
                res = change(x, y)
                if res[0] != '0':
                    res_i = int(res)
                    min_num = min(min_num, res_i)
                    max_num = max(max_num, res_i)
            x += 1
        return max_num - min_num
