class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_bacg]
        ) ->var_bacg:
        var_rgwu, var_wrnh = 1, var_osiz(arg_rcsn) // arg_xdvx
        while var_rgwu < var_wrnh:
            var_ayzf = var_wrnh - (var_wrnh - var_rgwu) // 2
            var_wnki = 0
            for var_egyk in arg_rcsn:
                var_wnki += var_dcmd(var_egyk, var_ayzf)
            if var_wnki // arg_xdvx >= var_ayzf:
                var_rgwu = var_ayzf
            else:
                var_wrnh = var_ayzf - 1
        return var_rgwu
