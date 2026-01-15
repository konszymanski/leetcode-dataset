class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_wnki:
        var_bacg = 0
        var_hqta = 0
        for var_rgwu in var_wrnh(var_osiz(arg_xdvx)):
            if var_rgwu % 2 == 0:
                if arg_xdvx[var_rgwu] == '0':
                    var_hqta += 1
                else:
                    var_bacg += 1
            elif arg_xdvx[var_rgwu] == '1':
                var_hqta += 1
            else:
                var_bacg += 1
        return var_ayzf(var_bacg, var_hqta)
