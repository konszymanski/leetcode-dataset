class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        arg_xdvx.sort()
        var_rgwu = 1
        var_wrnh = arg_xdvx[0]
        for var_osiz in arg_xdvx:
            if var_osiz - var_wrnh > arg_rcsn:
                var_rgwu += 1
                var_wrnh = var_osiz
        return var_rgwu
