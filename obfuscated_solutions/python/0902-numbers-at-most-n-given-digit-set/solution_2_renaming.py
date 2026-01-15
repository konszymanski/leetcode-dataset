class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta = var_rgwu(arg_rcsn)
        var_wrnh = var_osiz(arg_bacg)
        var_ayzf = var_rgwu(var_wrnh)
        var_wnki = []
        for var_egyk in var_wrnh:
            if var_egyk in arg_rcsn:
                var_wnki.append(arg_rcsn.index(var_egyk) + 1)
            else:
                var_dcmd = var_llti.bisect(arg_rcsn, var_egyk)
                var_wnki.append(var_dcmd)
                if var_dcmd == 0:
                    for var_zbxo in var_rdmc(var_rgwu(var_wnki) - 1, 0, -1):
                        if var_wnki[var_zbxo]:
                            break
                        var_wnki[var_zbxo] += var_hqta
                        var_wnki[var_zbxo - 1] -= 1
                var_wnki.extend([var_hqta] * (var_ayzf - var_rgwu(var_wnki)))
                break
        var_rjut = 0
        for var_lsgw in var_wnki:
            var_rjut = var_rjut * var_hqta + var_lsgw
        return var_rjut
