class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_hqta
        [var_bacg]]) ->var_bacg:
        var_rgwu = var_wrnh(var_bacg)
        var_osiz = 0
        var_ayzf = 0
        var_wnki = arg_xdvx
        for var_egyk in arg_rcsn:
            var_wnki = var_dcmd(var_wnki, var_egyk[0])
            var_rgwu[var_egyk[0]] += 1
            var_rgwu[var_egyk[1] + 1] -= 1
        var_ayzf += var_wnki - 1
        for var_llti in var_zbxo(var_rgwu.keys()):
            if var_osiz == 0:
                var_ayzf += var_llti - var_wnki
            var_osiz += var_rgwu[var_llti]
            var_wnki = var_llti
        var_ayzf += arg_xdvx - var_wnki + 1
        return var_ayzf
