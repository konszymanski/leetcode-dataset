class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = var_hqta(var_rgwu(arg_xdvx))
        var_wrnh = var_osiz(var_bacg)
        var_ayzf = [0] * var_wrnh
        var_ayzf[var_wrnh - 1] = var_wrnh - 1
        for var_wnki in var_egyk(var_wrnh - 2, -1, -1):
            var_ayzf[var_wnki] = var_wnki if var_bacg[var_wnki] > var_bacg[
                var_ayzf[var_wnki + 1]] else var_ayzf[var_wnki + 1]
        for var_wnki in var_egyk(var_wrnh):
            if var_bacg[var_wnki] < var_bacg[var_ayzf[var_wnki]]:
                var_bacg[var_wnki], var_bacg[var_ayzf[var_wnki]] = var_bacg[
                    var_ayzf[var_wnki]], var_bacg[var_wnki]
                return var_rcsn(''.join(var_bacg))
        return arg_xdvx
