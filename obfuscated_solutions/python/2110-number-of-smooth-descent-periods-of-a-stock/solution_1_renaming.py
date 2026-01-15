class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = 1
        var_osiz = 1
        for var_ayzf in var_wnki(1, var_hqta):
            if arg_xdvx[var_ayzf] == arg_xdvx[var_ayzf - 1] - 1:
                var_osiz += 1
            else:
                var_osiz = 1
            var_wrnh += var_osiz
        return var_wrnh
