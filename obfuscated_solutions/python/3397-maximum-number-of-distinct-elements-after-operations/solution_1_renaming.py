class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        arg_xdvx.sort()
        var_rgwu = 0
        var_wrnh = -var_osiz.inf
        for var_ayzf in arg_xdvx:
            var_wnki = var_egyk(var_dcmd(var_ayzf - arg_rcsn, var_wrnh + 1),
                var_ayzf + arg_rcsn)
            if var_wnki > var_wrnh:
                var_rgwu += 1
                var_wrnh = var_wnki
        return var_rgwu
