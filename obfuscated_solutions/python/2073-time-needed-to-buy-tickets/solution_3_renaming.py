class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = 0
        for var_wrnh in var_osiz(var_ayzf(arg_xdvx)):
            if var_wrnh <= arg_rcsn:
                var_rgwu += var_wnki(arg_xdvx[arg_rcsn], arg_xdvx[var_wrnh])
            else:
                var_rgwu += var_wnki(arg_xdvx[arg_rcsn] - 1, arg_xdvx[var_wrnh]
                    )
        return var_rgwu
