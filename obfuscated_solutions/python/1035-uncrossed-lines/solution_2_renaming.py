class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta = var_rgwu(arg_rcsn)
        var_wrnh = var_rgwu(arg_bacg)
        var_osiz = [([0] * (var_wrnh + 1)) for var_ayzf in var_wnki(
            var_hqta + 1)]
        for var_egyk in var_wnki(1, var_hqta + 1):
            for var_dcmd in var_wnki(1, var_wrnh + 1):
                if arg_rcsn[var_egyk - 1] == arg_bacg[var_dcmd - 1]:
                    var_osiz[var_egyk][var_dcmd] = 1 + var_osiz[var_egyk - 1][
                        var_dcmd - 1]
                else:
                    var_osiz[var_egyk][var_dcmd] = var_llti(var_osiz[
                        var_egyk][var_dcmd - 1], var_osiz[var_egyk - 1][
                        var_dcmd])
        return var_osiz[var_hqta][var_wrnh]
