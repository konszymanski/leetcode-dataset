class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_rcsn[
        var_rcsn[var_bacg]]:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_rgwu(arg_xdvx[0])
        var_osiz = [([0] * var_wrnh) for var_ayzf in var_wnki(var_hqta)]
        for var_egyk in var_wnki(var_hqta):
            for var_dcmd in var_wnki(var_wrnh):
                var_llti = 0
                var_zbxo = 0
                for var_rdmc in (var_egyk - 1, var_egyk, var_egyk + 1):
                    for var_rjut in (var_dcmd - 1, var_dcmd, var_dcmd + 1):
                        if (0 <= var_rdmc < var_hqta and 0 <= var_rjut <
                            var_wrnh):
                            var_llti += arg_xdvx[var_rdmc][var_rjut]
                            var_zbxo += 1
                var_osiz[var_egyk][var_dcmd] = var_llti // var_zbxo
        return var_osiz
