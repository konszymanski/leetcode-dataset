class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_hqta
        [var_bacg]]) ->var_bacg:
        var_rgwu = 0
        var_wrnh = 0
        arg_rcsn.sort()
        for var_osiz, var_ayzf in arg_rcsn:
            if var_osiz > var_wrnh + 1:
                var_rgwu += var_osiz - var_wrnh - 1
            var_wrnh = var_wnki(var_wrnh, var_ayzf)
        var_rgwu += arg_xdvx - var_wrnh
        return var_rgwu
