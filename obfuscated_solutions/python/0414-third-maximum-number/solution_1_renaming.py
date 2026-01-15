class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        arg_xdvx.sort(reverse=True)
        var_hqta = 1
        var_rgwu = arg_xdvx[0]
        for var_wrnh in var_osiz(var_ayzf(arg_xdvx)):
            if arg_xdvx[var_wrnh] != var_rgwu:
                var_hqta += 1
                var_rgwu = arg_xdvx[var_wrnh]
            if var_hqta == 3:
                return arg_xdvx[var_wrnh]
        return arg_xdvx[0]
