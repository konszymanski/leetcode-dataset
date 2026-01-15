class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_rgwu(arg_xdvx[0])
        var_osiz = [0] * var_wrnh
        var_ayzf = 0
        for var_wnki in var_egyk(var_hqta):
            var_dcmd = arg_xdvx[var_wnki][:]
            for var_llti in var_egyk(var_wrnh):
                if var_dcmd[var_llti] != 0:
                    var_dcmd[var_llti] += var_osiz[var_llti]
            var_zbxo = var_rdmc(var_dcmd, reverse=True)
            for var_rjut in var_egyk(var_wrnh):
                var_ayzf = var_lsgw(var_ayzf, var_zbxo[var_rjut] * (
                    var_rjut + 1))
            var_osiz = var_dcmd
        return var_ayzf
