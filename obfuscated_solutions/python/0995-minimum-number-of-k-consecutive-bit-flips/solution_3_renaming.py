class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = 0
        var_wrnh = 0
        for var_osiz in var_ayzf(var_wnki(arg_xdvx)):
            if var_osiz >= arg_rcsn and arg_xdvx[var_osiz - arg_rcsn] == 2:
                var_rgwu -= 1
            if var_rgwu % 2 == arg_xdvx[var_osiz]:
                if var_osiz + arg_rcsn > var_wnki(arg_xdvx):
                    return -1
                arg_xdvx[var_osiz] = 2
                var_rgwu += 1
                var_wrnh += 1
        return var_wrnh
