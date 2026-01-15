class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_rjut:
        var_rgwu = var_wrnh(arg_xdvx)
        if var_rgwu % arg_rcsn != 0:
            return False
        var_osiz = var_ayzf(arg_xdvx)
        var_wnki = var_egyk(var_osiz.keys())
        var_dcmd.heapify(var_wnki)
        while var_wnki:
            var_llti = var_wnki[0]
            for var_zbxo in var_rdmc(arg_rcsn):
                if var_osiz[var_llti + var_zbxo] == 0:
                    return False
                var_osiz[var_llti + var_zbxo] -= 1
                if var_osiz[var_llti + var_zbxo] == 0:
                    if var_llti + var_zbxo != var_dcmd.heappop(var_wnki):
                        return False
        return True
