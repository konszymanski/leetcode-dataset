class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = var_wrnh(var_bacg) - 2
        for var_osiz in var_ayzf(var_wrnh(var_bacg) // 2):
            var_bacg[var_osiz], var_bacg[var_rgwu - var_osiz] = var_bacg[
                var_rgwu - var_osiz], var_bacg[var_osiz]
        return ''.join(var_bacg)
