class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta) ->var_bacg:
        if arg_rcsn == 1:
            return arg_xdvx
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = ''
        for var_ayzf in var_wnki(var_rgwu):
            var_osiz = var_egyk(var_osiz, arg_xdvx[var_ayzf:var_dcmd(
                var_ayzf + var_rgwu - arg_rcsn + 1, var_rgwu)])
        return var_osiz
