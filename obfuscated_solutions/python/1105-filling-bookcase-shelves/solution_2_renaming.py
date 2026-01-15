class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_bacg[var_hqta]],
        arg_rcsn: var_hqta) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = [0] * (var_rgwu + 1)
        var_osiz[0] = 0
        var_osiz[1] = arg_xdvx[0][1]
        for var_ayzf in var_wnki(2, var_rgwu + 1):
            var_egyk = arg_rcsn - arg_xdvx[var_ayzf - 1][0]
            var_dcmd = arg_xdvx[var_ayzf - 1][1]
            var_osiz[var_ayzf] = arg_xdvx[var_ayzf - 1][1] + var_osiz[
                var_ayzf - 1]
            var_llti = var_ayzf - 1
            while var_llti > 0 and var_egyk - arg_xdvx[var_llti - 1][0] >= 0:
                var_dcmd = var_zbxo(var_dcmd, arg_xdvx[var_llti - 1][1])
                var_egyk -= arg_xdvx[var_llti - 1][0]
                var_osiz[var_ayzf] = var_rdmc(var_osiz[var_ayzf], var_dcmd +
                    var_osiz[var_llti - 1])
                var_llti -= 1
        return var_osiz[var_rgwu]
