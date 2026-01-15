class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_wnki:
        var_hqta = var_rgwu(arg_xdvx)
        if var_hqta <= 1:
            return True
        var_wrnh = 0
        for var_osiz in var_ayzf(1, var_hqta):
            if arg_xdvx[var_osiz] < arg_xdvx[var_osiz - 1]:
                var_wrnh += 1
                if var_wrnh > 1:
                    return False
        if arg_xdvx[0] < arg_xdvx[var_hqta - 1]:
            var_wrnh += 1
        return var_wrnh <= 1
