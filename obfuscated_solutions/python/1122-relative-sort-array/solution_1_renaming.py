class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_bacg[var_hqta]:
        var_rgwu = []
        for var_wrnh in arg_rcsn:
            for var_osiz in var_ayzf(var_wnki(arg_xdvx)):
                if arg_xdvx[var_osiz] == var_wrnh:
                    var_rgwu.append(arg_xdvx[var_osiz])
                    arg_xdvx[var_osiz] = -1
        arg_xdvx.sort()
        for var_wrnh in arg_xdvx:
            if var_wrnh != -1:
                var_rgwu.append(var_wrnh)
        return var_rgwu
