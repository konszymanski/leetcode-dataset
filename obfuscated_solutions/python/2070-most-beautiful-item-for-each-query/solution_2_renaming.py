class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = [0] * var_hqta(arg_rcsn)
        items.sort(key=lambda x: var_rgwu[0])
        var_wrnh = [[arg_rcsn[var_osiz], var_osiz] for var_osiz in var_ayzf
            (var_hqta(arg_rcsn))]
        var_wrnh.sort(key=lambda x: var_rgwu[0])
        var_wnki = 0
        var_egyk = 0
        for var_osiz in var_ayzf(var_hqta(arg_rcsn)):
            var_dcmd = var_wrnh[var_osiz][0]
            var_llti = var_wrnh[var_osiz][1]
            while var_wnki < var_hqta(items) and items[var_wnki][0
                ] <= var_dcmd:
                var_egyk = var_zbxo(var_egyk, items[var_wnki][1])
                var_wnki += 1
            var_bacg[var_llti] = var_egyk
        return var_bacg
