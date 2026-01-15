class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = var_bacg(arg_xdvx)
        values = arg_xdvx.copy()
        for var_hqta in var_rgwu(var_rcsn - 1):
            if values[var_hqta] <= values[var_hqta + 1]:
                continue
            elif var_wrnh(values[var_hqta]).count('1') == var_wrnh(values[
                var_hqta + 1]).count('1'):
                var_osiz = values[var_hqta]
                values[var_hqta] = values[var_hqta + 1]
                values[var_hqta + 1] = var_osiz
            else:
                return False
        for var_hqta in var_rgwu(var_rcsn - 1, 0, -1):
            if values[var_hqta] >= values[var_hqta - 1]:
                continue
            elif var_wrnh(values[var_hqta]).count('1') == var_wrnh(values[
                var_hqta - 1]).count('1'):
                var_osiz = values[var_hqta]
                values[var_hqta] = values[var_hqta - 1]
                values[var_hqta - 1] = var_osiz
            else:
                return False
        return True
