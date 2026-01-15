class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = [0] * 100
        for var_bacg in arg_xdvx:
            var_rcsn[var_bacg - 1] += 1
        var_rcsn.sort()
        var_hqta = var_rgwu(var_rcsn) - 1
        var_wrnh = var_rcsn[var_hqta]
        while var_hqta > 0 and var_rcsn[var_hqta] == var_rcsn[var_hqta - 1]:
            var_wrnh += var_rcsn[var_hqta]
            var_hqta -= 1
        return var_wrnh
