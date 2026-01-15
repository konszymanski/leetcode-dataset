class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = 0
        for var_ayzf in var_wnki(var_rgwu - 1):
            for var_egyk in var_wnki(var_ayzf + 1, var_rgwu):
                if var_ayzf * var_egyk % arg_rcsn == 0 and arg_xdvx[var_ayzf
                    ] == arg_xdvx[var_egyk]:
                    var_osiz += 1
        return var_osiz
