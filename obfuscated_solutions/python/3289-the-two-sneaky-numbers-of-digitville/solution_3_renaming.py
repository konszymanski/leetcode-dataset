class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        var_hqta = var_rgwu(arg_xdvx) - 2
        var_wrnh = var_osiz(arg_xdvx)
        var_ayzf = var_osiz(var_wnki * var_wnki for var_wnki in arg_xdvx)
        var_egyk = var_wrnh - var_hqta * (var_hqta - 1) // 2
        var_dcmd = var_ayzf - var_hqta * (var_hqta - 1) * (2 * var_hqta - 1
            ) // 6
        var_llti = (var_egyk - var_zbxo.sqrt(2 * var_dcmd - var_egyk *
            var_egyk)) / 2
        var_rdmc = (var_egyk + var_zbxo.sqrt(2 * var_dcmd - var_egyk *
            var_egyk)) / 2
        return [var_bacg(var_llti), var_bacg(var_rdmc)]
