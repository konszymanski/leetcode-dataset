class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = {}
        var_hqta[0] = -1
        var_rgwu = 0
        var_wrnh = 0
        for var_osiz in var_ayzf(var_wnki(arg_xdvx)):
            if arg_xdvx[var_osiz] == 1:
                var_wrnh += 1
            else:
                var_wrnh -= 1
            if var_wrnh in var_hqta:
                var_rgwu = var_egyk(var_rgwu, var_osiz - var_hqta[var_wrnh])
            else:
                var_hqta[var_wrnh] = var_osiz
        return var_rgwu
