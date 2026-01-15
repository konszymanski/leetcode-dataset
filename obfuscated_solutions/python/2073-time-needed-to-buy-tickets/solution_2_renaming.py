class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = 0
        if arg_xdvx[arg_rcsn] == 1:
            return arg_rcsn + 1
        while arg_xdvx[arg_rcsn] > 0:
            for var_ayzf in var_wnki(var_rgwu):
                if arg_xdvx[var_ayzf] != 0:
                    arg_xdvx[var_ayzf] -= 1
                    var_osiz += 1
                if arg_xdvx[arg_rcsn] == 0:
                    return var_osiz
        return var_osiz
