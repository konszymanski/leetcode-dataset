class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_rgwu]) ->var_rgwu:
        var_wrnh = [0] * (var_osiz(arg_rcsn) + 1)
        var_wrnh[1] = arg_rcsn[0]
        for var_ayzf in var_wnki(1, var_osiz(arg_rcsn)):
            var_wrnh[var_ayzf + 1] = var_wrnh[var_ayzf] + arg_rcsn[var_ayzf]
        var_egyk = {}
        var_dcmd = {}
        for var_ayzf in var_wnki(var_osiz(arg_xdvx)):
            for var_llti in arg_xdvx[var_ayzf]:
                var_egyk[var_llti] = var_ayzf
                var_dcmd[var_llti] = var_dcmd.get(var_llti, 0) + 1
        var_zbxo = 'MPG'
        var_rdmc = 0
        for var_llti in var_zbxo:
            if var_llti in var_dcmd:
                var_rdmc += var_wrnh[var_egyk[var_llti]] + var_dcmd[var_llti]
        return var_rdmc
