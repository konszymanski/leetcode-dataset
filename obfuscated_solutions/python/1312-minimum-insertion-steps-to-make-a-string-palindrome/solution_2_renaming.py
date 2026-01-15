class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_hqta,
        arg_bacg: var_rgwu) ->var_rgwu:
        var_wrnh = [[(0) for var_osiz in var_ayzf(arg_bacg + 1)] for
            var_osiz in var_ayzf(arg_bacg + 1)]
        for var_wnki in var_ayzf(arg_bacg + 1):
            for var_egyk in var_ayzf(arg_bacg + 1):
                if var_wnki == 0 or var_egyk == 0:
                    var_wrnh[var_wnki][var_egyk] = 0
                elif arg_xdvx[var_wnki - 1] == arg_rcsn[var_egyk - 1]:
                    var_wrnh[var_wnki][var_egyk] = 1 + var_wrnh[var_wnki - 1][
                        var_egyk - 1]
                else:
                    var_wrnh[var_wnki][var_egyk] = var_dcmd(var_wrnh[
                        var_wnki - 1][var_egyk], var_wrnh[var_wnki][
                        var_egyk - 1])
        return var_wrnh[arg_bacg][arg_bacg]

    def func_llti(arg_ihhe, arg_zbxo: var_hqta) ->var_rgwu:
        arg_bacg = var_rdmc(arg_zbxo)
        var_rjut = arg_zbxo[::-1]
        return arg_bacg - arg_ihhe.lcs(arg_zbxo, var_rjut, arg_bacg)
