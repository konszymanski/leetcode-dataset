class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_ayzf:
        for var_hqta in var_rgwu(var_wrnh(arg_xdvx) - 2):
            var_osiz = arg_xdvx[var_hqta] * arg_xdvx[var_hqta + 1] * arg_xdvx[
                var_hqta + 2]
            if var_osiz % 2 == 1:
                return True
        return False
