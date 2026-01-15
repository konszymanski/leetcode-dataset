class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_egyk:
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = [0] * (var_bacg + 1)
        var_wrnh = 0
        for var_osiz in var_ayzf(var_bacg):
            if arg_xdvx[var_osiz] == 'b':
                var_rgwu[var_osiz + 1] = var_rgwu[var_osiz]
                var_wrnh += 1
            else:
                var_rgwu[var_osiz + 1] = var_wnki(var_rgwu[var_osiz] + 1,
                    var_wrnh)
        return var_rgwu[var_bacg]
