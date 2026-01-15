class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_wnki:
        var_bacg = -1
        for var_hqta in var_rgwu(var_wrnh(arg_xdvx)):
            for var_osiz in var_rgwu(var_hqta + 1, var_wrnh(arg_xdvx)):
                if arg_xdvx[var_hqta] == arg_xdvx[var_osiz]:
                    var_bacg = var_ayzf(var_bacg, var_osiz - var_hqta - 1)
        return var_bacg
