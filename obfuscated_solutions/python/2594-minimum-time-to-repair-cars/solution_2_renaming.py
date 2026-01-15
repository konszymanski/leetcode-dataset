class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu, var_wrnh = 1, arg_rcsn * arg_rcsn * arg_xdvx[0]
        while var_rgwu < var_wrnh:
            var_osiz = (var_rgwu + var_wrnh) // 2
            var_ayzf = var_wnki(var_hqta((var_osiz / var_egyk) ** 0.5) for
                var_egyk in arg_xdvx)
            if var_ayzf < arg_rcsn:
                var_rgwu = var_osiz + 1
            else:
                var_wrnh = var_osiz
        return var_rgwu
