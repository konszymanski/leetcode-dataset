class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_rcsn[
        var_bacg]:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_hqta * var_hqta
        var_osiz = var_ayzf(var_wnki for var_egyk in arg_xdvx for var_wnki in
            var_egyk)
        var_dcmd = var_ayzf(var_wnki * var_wnki for var_egyk in arg_xdvx for
            var_wnki in var_egyk)
        var_llti = var_osiz - var_wrnh * (var_wrnh + 1) // 2
        var_zbxo = var_dcmd - var_wrnh * (var_wrnh + 1) * (2 * var_wrnh + 1
            ) // 6
        var_rdmc = (var_zbxo // var_llti + var_llti) // 2
        var_rjut = (var_zbxo // var_llti - var_llti) // 2
        return [var_rdmc, var_rjut]
