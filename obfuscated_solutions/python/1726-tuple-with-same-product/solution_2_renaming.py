class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = var_bacg(arg_xdvx)
        var_hqta = []
        var_rgwu = 0
        for var_wrnh in var_osiz(var_rcsn):
            for var_ayzf in var_osiz(var_wrnh + 1, var_rcsn):
                var_hqta.append(arg_xdvx[var_wrnh] * arg_xdvx[var_ayzf])
        var_hqta.sort()
        var_wnki = -1
        var_egyk = 0
        for var_dcmd in var_osiz(var_bacg(var_hqta)):
            if var_hqta[var_dcmd] == var_wnki:
                var_egyk += 1
            else:
                var_llti = (var_egyk - 1) * var_egyk // 2
                var_rgwu += 8 * var_llti
                var_wnki = var_hqta[var_dcmd]
                var_egyk = 1
        var_llti = (var_egyk - 1) * var_egyk // 2
        var_rgwu += 8 * var_llti
        return var_rgwu
