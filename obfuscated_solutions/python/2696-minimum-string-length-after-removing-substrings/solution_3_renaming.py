class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_egyk:
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = 0
        for var_wrnh in var_osiz(var_ayzf(arg_xdvx)):
            var_bacg[var_rgwu] = var_bacg[var_wrnh]
            if var_rgwu > 0 and var_bacg[var_rgwu - 1] in 'AC' and var_wnki(
                var_bacg[var_rgwu]) == var_wnki(var_bacg[var_rgwu - 1]) + 1:
                var_rgwu -= 1
            else:
                var_rgwu += 1
        return var_rgwu
