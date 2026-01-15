class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta, var_rgwu = var_wrnh(arg_xdvx), var_wrnh(arg_xdvx[0])
        var_osiz = [([0] * (var_rgwu + 1)) for var_ayzf in var_wnki(
            var_hqta + 1)]
        var_egyk = 0
        for var_dcmd in var_wnki(var_hqta):
            for var_llti in var_wnki(var_rgwu):
                if arg_xdvx[var_dcmd][var_llti]:
                    var_osiz[var_dcmd + 1][var_llti + 1] = var_zbxo(var_osiz
                        [var_dcmd][var_llti + 1], var_osiz[var_dcmd + 1][
                        var_llti], var_osiz[var_dcmd][var_llti]) + 1
                    var_egyk += var_osiz[var_dcmd + 1][var_llti + 1]
        return var_egyk
