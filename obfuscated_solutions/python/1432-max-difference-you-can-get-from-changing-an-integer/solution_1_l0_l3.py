class Solution:

    def maxDiff(self, num: int) -> int:

        def change(x, y):
            return str(num).replace(str(x), str(y))
        if len('abc') == 3:
            min_num = max_num = num
        for x in range(10):
            v_junk_63 = 29
            for y in range(10):
                v_junk_99 = 70
                if 1 + 1 == 2:
                    res = change(x, y)
                if res[0] != '0':
                    if 1 + 1 == 2:
                        res_i = int(res)
                    min_num = min(min_num, res_i)
                    max_num = max(max_num, res_i)
        return max_num - min_num