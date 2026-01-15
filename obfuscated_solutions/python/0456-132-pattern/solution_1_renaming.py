class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_wnki:
        for var_hqta in var_rgwu(var_wrnh(arg_xdvx) - 2):
            for var_osiz in var_rgwu(var_hqta + 1, var_wrnh(arg_xdvx) - 1):
                for var_ayzf in var_rgwu(var_osiz + 1, var_wrnh(arg_xdvx)):
                    if arg_xdvx[var_hqta] < arg_xdvx[var_ayzf] < arg_xdvx[
                        var_osiz]:
                        return True
        return False
