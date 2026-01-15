class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta = arg_xdvx.find(arg_rcsn)
        if var_hqta == -1:
            return arg_xdvx
        var_rgwu = ''
        for var_wrnh in var_osiz(0, var_ayzf(arg_xdvx)):
            if var_wrnh <= var_hqta:
                var_rgwu += arg_xdvx[var_hqta - var_wrnh]
            else:
                var_rgwu += arg_xdvx[var_wrnh]
        return var_rgwu
