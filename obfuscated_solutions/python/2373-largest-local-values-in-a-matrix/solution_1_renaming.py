class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta = 0
        for var_rgwu in var_wrnh(arg_rcsn, arg_rcsn + 3):
            for var_osiz in var_wrnh(arg_bacg, arg_bacg + 3):
                var_hqta = var_ayzf(var_hqta, arg_xdvx[var_rgwu][var_osiz])
        return var_hqta

    def func_wnki(arg_ihhe, arg_xdvx):
        var_egyk = var_dcmd(arg_xdvx)
        var_llti = [([0] * (var_egyk - 2)) for var_zbxo in var_wrnh(
            var_egyk - 2)]
        for var_rgwu in var_wrnh(var_egyk - 2):
            for var_osiz in var_wrnh(var_egyk - 2):
                var_llti[var_rgwu][var_osiz] = arg_ihhe.find_max(arg_xdvx,
                    var_rgwu, var_osiz)
        return var_llti
