class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = var_ayzf(arg_xdvx)
        var_wnki = [0] * (var_osiz + 1)
        for var_egyk in var_dcmd(var_rgwu):
            for var_llti in var_dcmd(var_egyk + 1, var_rgwu):
                var_zbxo = var_rdmc(arg_xdvx[var_egyk] - arg_xdvx[var_llti])
                var_wnki[var_zbxo] += 1
        for var_rjut in var_dcmd(var_osiz + 1):
            arg_rcsn -= var_wnki[var_rjut]
            if arg_rcsn <= 0:
                return var_rjut
        return -1
