class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        if var_rgwu == 0:
            return 0
        var_osiz = 0
        for var_ayzf in var_wnki(var_rgwu - 1):
            var_osiz += var_egyk(arg_xdvx[var_ayzf + 1] - arg_xdvx[var_ayzf
                ], arg_rcsn)
        return var_osiz + arg_rcsn
