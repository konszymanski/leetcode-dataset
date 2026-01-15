class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = [0] * (var_rgwu + 1)
        var_ayzf = [var_wnki] * (var_rgwu + 1)
        var_ayzf[0] = 0
        for var_egyk in var_dcmd(var_rgwu - 1, -1, -1):
            var_osiz = [0] * (var_rgwu + 1)
            for var_llti in var_dcmd(1, var_rgwu + 1):
                var_zbxo = arg_xdvx[var_egyk] + var_ayzf[var_rdmc(0, 
                    var_llti - 1 - arg_rcsn[var_egyk])]
                var_rjut = var_ayzf[var_llti]
                var_osiz[var_llti] = var_lsgw(var_zbxo, var_rjut)
            var_ayzf = var_osiz
        return var_osiz[var_rgwu]
