class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_egyk:
        var_bacg = arg_xdvx.count('1')
        var_hqta = 0
        var_rgwu = 0
        for var_wrnh in var_osiz(var_ayzf(arg_xdvx) - 1):
            if arg_xdvx[var_wrnh] == '1':
                var_bacg -= 1
            else:
                var_hqta += 1
            var_rgwu = var_wnki(var_rgwu, var_hqta + var_bacg)
        return var_rgwu
