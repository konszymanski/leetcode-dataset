class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta, var_rgwu = var_wrnh(arg_xdvx), var_wrnh(arg_xdvx[0])
        var_osiz = [([var_ayzf('inf')] * var_rgwu) for var_wnki in var_egyk
            (var_hqta)]
        var_osiz[0][0] = 0
        while True:
            var_dcmd = [var_llti[:] for var_llti in var_osiz]
            for var_llti in var_egyk(var_hqta):
                for var_zbxo in var_egyk(var_rgwu):
                    if var_llti > 0:
                        var_osiz[var_llti][var_zbxo] = var_rdmc(var_osiz[
                            var_llti][var_zbxo], var_osiz[var_llti - 1][
                            var_zbxo] + (0 if arg_xdvx[var_llti - 1][
                            var_zbxo] == 3 else 1))
                    if var_zbxo > 0:
                        var_osiz[var_llti][var_zbxo] = var_rdmc(var_osiz[
                            var_llti][var_zbxo], var_osiz[var_llti][
                            var_zbxo - 1] + (0 if arg_xdvx[var_llti][
                            var_zbxo - 1] == 1 else 1))
            for var_llti in var_egyk(var_hqta - 1, -1, -1):
                for var_zbxo in var_egyk(var_rgwu - 1, -1, -1):
                    if var_llti < var_hqta - 1:
                        var_osiz[var_llti][var_zbxo] = var_rdmc(var_osiz[
                            var_llti][var_zbxo], var_osiz[var_llti + 1][
                            var_zbxo] + (0 if arg_xdvx[var_llti + 1][
                            var_zbxo] == 4 else 1))
                    if var_zbxo < var_rgwu - 1:
                        var_osiz[var_llti][var_zbxo] = var_rdmc(var_osiz[
                            var_llti][var_zbxo], var_osiz[var_llti][
                            var_zbxo + 1] + (0 if arg_xdvx[var_llti][
                            var_zbxo + 1] == 2 else 1))
            if var_osiz == var_dcmd:
                break
        return var_osiz[var_hqta - 1][var_rgwu - 1]
