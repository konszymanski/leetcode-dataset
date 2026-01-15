class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_wnki:
        var_bacg = {}
        var_hqta = -1
        for var_rgwu in var_wrnh(var_osiz(arg_xdvx)):
            if arg_xdvx[var_rgwu] in var_bacg:
                var_hqta = var_ayzf(var_hqta, var_rgwu - var_bacg[arg_xdvx[
                    var_rgwu]] - 1)
            else:
                var_bacg[arg_xdvx[var_rgwu]] = var_rgwu
        return var_hqta
