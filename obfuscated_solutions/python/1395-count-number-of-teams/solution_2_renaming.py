class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = 0
        var_osiz = [([0] * 4) for var_ayzf in var_wnki(var_hqta)]
        var_egyk = [([0] * 4) for var_ayzf in var_wnki(var_hqta)]
        for var_dcmd in var_wnki(var_hqta):
            var_osiz[var_dcmd][1] = 1
            var_egyk[var_dcmd][1] = 1
        for var_llti in var_wnki(2, 4):
            for var_dcmd in var_wnki(var_hqta):
                for var_zbxo in var_wnki(var_dcmd + 1, var_hqta):
                    if arg_xdvx[var_zbxo] > arg_xdvx[var_dcmd]:
                        var_osiz[var_zbxo][var_llti] += var_osiz[var_dcmd][
                            var_llti - 1]
                    if arg_xdvx[var_zbxo] < arg_xdvx[var_dcmd]:
                        var_egyk[var_zbxo][var_llti] += var_egyk[var_dcmd][
                            var_llti - 1]
        for var_dcmd in var_wnki(var_hqta):
            var_wrnh += var_osiz[var_dcmd][3] + var_egyk[var_dcmd][3]
        return var_wrnh
