class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta = var_rgwu(arg_rcsn)
        var_wrnh = var_rgwu(arg_bacg)
        var_osiz = [0] * (var_wrnh + 1)
        var_ayzf = [0] * (var_wrnh + 1)
        for var_wnki in var_egyk(1, var_hqta + 1):
            for var_dcmd in var_egyk(1, var_wrnh + 1):
                if arg_rcsn[var_wnki - 1] == arg_bacg[var_dcmd - 1]:
                    var_osiz[var_dcmd] = 1 + var_ayzf[var_dcmd - 1]
                else:
                    var_osiz[var_dcmd] = var_llti(var_osiz[var_dcmd - 1],
                        var_ayzf[var_dcmd])
            var_ayzf = var_osiz[:]
        return var_osiz[var_wrnh]
