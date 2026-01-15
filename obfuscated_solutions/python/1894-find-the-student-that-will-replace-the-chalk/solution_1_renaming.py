class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = 0
        for var_wrnh in var_osiz(var_ayzf(arg_xdvx)):
            var_rgwu += arg_xdvx[var_wrnh]
            if var_rgwu > arg_rcsn:
                break
        arg_rcsn = arg_rcsn % var_rgwu
        for var_wrnh in var_osiz(var_ayzf(arg_xdvx)):
            if arg_rcsn < arg_xdvx[var_wrnh]:
                return var_wrnh
            arg_rcsn -= arg_xdvx[var_wrnh]
        return 0
