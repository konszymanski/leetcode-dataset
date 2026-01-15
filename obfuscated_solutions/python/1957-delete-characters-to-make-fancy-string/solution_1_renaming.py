class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = arg_xdvx[0]
        var_hqta = 1
        var_rgwu = arg_xdvx[0]
        for var_wrnh in var_osiz(1, var_ayzf(arg_xdvx)):
            if arg_xdvx[var_wrnh] == var_bacg:
                var_hqta += 1
            else:
                var_bacg = arg_xdvx[var_wrnh]
                var_hqta = 1
            if var_hqta < 3:
                var_rgwu += arg_xdvx[var_wrnh]
        return var_rgwu
