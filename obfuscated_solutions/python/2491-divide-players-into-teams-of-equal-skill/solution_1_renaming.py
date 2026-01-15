class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        arg_xdvx.sort()
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = 0
        var_osiz = arg_xdvx[0] + arg_xdvx[-1]
        for var_ayzf in var_wnki(var_hqta // 2):
            if arg_xdvx[var_ayzf] + arg_xdvx[-var_ayzf - 1] != var_osiz:
                return -1
            var_wrnh += arg_xdvx[var_ayzf] * arg_xdvx[-var_ayzf - 1]
        return var_wrnh
