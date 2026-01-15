class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = [([False] * var_bacg) for var_wrnh in var_osiz(var_bacg)]
        var_ayzf = [0, 0]
        for var_wnki in var_osiz(var_bacg):
            var_rgwu[var_wnki][var_wnki] = True
        for var_wnki in var_osiz(var_bacg - 1):
            if arg_xdvx[var_wnki] == arg_xdvx[var_wnki + 1]:
                var_rgwu[var_wnki][var_wnki + 1] = True
                var_ayzf = [var_wnki, var_wnki + 1]
        for var_egyk in var_osiz(2, var_bacg):
            for var_wnki in var_osiz(var_bacg - var_egyk):
                var_dcmd = var_wnki + var_egyk
                if arg_xdvx[var_wnki] == arg_xdvx[var_dcmd] and var_rgwu[
                    var_wnki + 1][var_dcmd - 1]:
                    var_rgwu[var_wnki][var_dcmd] = True
                    var_ayzf = [var_wnki, var_dcmd]
        var_wnki, var_dcmd = var_ayzf
        return arg_xdvx[var_wnki:var_dcmd + 1]
