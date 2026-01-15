class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = 0
        for var_osiz in var_ayzf(var_hqta):
            var_wrnh += arg_xdvx[var_osiz][var_osiz]
            var_wrnh += arg_xdvx[var_hqta - 1 - var_osiz][var_osiz]
        if var_hqta % 2 != 0:
            var_wrnh -= arg_xdvx[var_hqta // 2][var_hqta // 2]
        return var_wrnh
