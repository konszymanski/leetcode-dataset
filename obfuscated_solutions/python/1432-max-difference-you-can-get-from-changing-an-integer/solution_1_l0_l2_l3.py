class Solution:

    def maxDiff(self, num: int) -> int:

        def change(x, y):
            return str(num).replace(str(x), str(y))
        min_num = max_num = num
        for x in range(10):
            v_junk_53 = 14
            for y in range(10):
                v_junk_29 = 28
                if 1 + 1 == 2:
                    res = change(x, y)
                if res[0] != '0':
                    res_i = int(res)
                    if len('abc') == 3:
                        min_num = min(min_num, res_i)
                    max_num = max(max_num, res_i)
        return max_num - min_num