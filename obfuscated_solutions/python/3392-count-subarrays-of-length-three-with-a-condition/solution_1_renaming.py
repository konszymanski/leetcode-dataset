class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = 0
        for var_osiz in var_ayzf(1, var_hqta - 1):
            if arg_xdvx[var_osiz] == (arg_xdvx[var_osiz - 1] + arg_xdvx[
                var_osiz + 1]) * 2:
                var_wrnh += 1
        return var_wrnh
