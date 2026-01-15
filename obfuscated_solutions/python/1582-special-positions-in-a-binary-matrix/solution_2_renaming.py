class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_rgwu(arg_xdvx[0])
        var_osiz = [0] * var_hqta
        var_ayzf = [0] * var_wrnh
        for var_wnki in var_egyk(var_hqta):
            for var_dcmd in var_egyk(var_wrnh):
                if arg_xdvx[var_wnki][var_dcmd] == 1:
                    var_osiz[var_wnki] += 1
                    var_ayzf[var_dcmd] += 1
        var_llti = 0
        for var_wnki in var_egyk(var_hqta):
            for var_dcmd in var_egyk(var_wrnh):
                if arg_xdvx[var_wnki][var_dcmd] == 1:
                    if var_osiz[var_wnki] == 1 and var_ayzf[var_dcmd] == 1:
                        var_llti += 1
        return var_llti
