class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = [var_osiz for var_osiz in var_ayzf(var_hqta)]
        var_wrnh.sort(key=lambda i: (arg_xdvx[var_osiz], var_osiz))
        var_wnki = var_hqta
        var_egyk = 0
        for var_osiz in var_wrnh:
            var_egyk = var_dcmd(var_egyk, var_osiz - var_wnki)
            var_wnki = var_llti(var_wnki, var_osiz)
        return var_egyk
