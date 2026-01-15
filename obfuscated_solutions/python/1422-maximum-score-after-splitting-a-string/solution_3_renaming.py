class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_dcmd:
        var_bacg = 0
        var_hqta = 0
        var_rgwu = -var_wrnh
        for var_osiz in var_ayzf(var_wnki(arg_xdvx) - 1):
            if arg_xdvx[var_osiz] == '1':
                var_bacg += 1
            else:
                var_hqta += 1
            var_rgwu = var_egyk(var_rgwu, var_hqta - var_bacg)
        if arg_xdvx[-1] == '1':
            var_bacg += 1
        return var_rgwu + var_bacg
