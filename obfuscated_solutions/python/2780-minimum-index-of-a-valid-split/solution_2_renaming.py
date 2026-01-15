class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = arg_xdvx[0]
        var_rgwu = 0
        var_wrnh = 0
        var_osiz = var_ayzf(arg_xdvx)
        for var_wnki in arg_xdvx:
            if var_wnki == var_hqta:
                var_rgwu += 1
            else:
                var_rgwu -= 1
            if var_rgwu == 0:
                var_hqta = var_wnki
                var_rgwu = 1
        for var_wnki in arg_xdvx:
            if var_wnki == var_hqta:
                var_wrnh += 1
        var_rgwu = 0
        for var_egyk in var_dcmd(var_osiz):
            if arg_xdvx[var_egyk] == var_hqta:
                var_rgwu += 1
            var_llti = var_wrnh - var_rgwu
            if (var_rgwu * 2 > var_egyk + 1 and var_llti * 2 > var_osiz -
                var_egyk - 1):
                return var_egyk
        return -1
