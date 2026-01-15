class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_bacg[var_hqta]],
        arg_rcsn: var_hqta) ->var_hqta:
        var_rgwu = []
        var_wrnh = 0
        for var_osiz in var_ayzf(var_wnki(arg_xdvx)):
            for var_egyk in var_ayzf(var_wnki(arg_xdvx[0])):
                if arg_xdvx[var_osiz][var_egyk] % arg_rcsn != arg_xdvx[0][0
                    ] % arg_rcsn:
                    return -1
                var_rgwu.append(arg_xdvx[var_osiz][var_egyk])
        var_rgwu.sort()
        var_dcmd = var_wnki(var_rgwu)
        var_llti = 0
        var_zbxo = var_dcmd - 1
        while var_llti < var_zbxo:
            if var_llti < var_dcmd - var_zbxo - 1:
                var_rdmc = (var_llti + 1) * (var_rgwu[var_llti + 1] -
                    var_rgwu[var_llti]) // arg_rcsn
                var_wrnh += var_rdmc
                var_llti += 1
            else:
                var_rjut = (var_dcmd - var_zbxo) * (var_rgwu[var_zbxo] -
                    var_rgwu[var_zbxo - 1]) // arg_rcsn
                var_wrnh += var_rjut
                var_zbxo -= 1
        return var_wrnh
