class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = [0] * 24
        for var_rgwu in var_wrnh(24):
            for var_osiz in arg_xdvx:
                if var_osiz & 1 << var_rgwu != 0:
                    var_hqta[var_rgwu] += 1
        return var_ayzf(var_hqta)
