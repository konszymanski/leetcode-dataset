class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh.bisect_right(arg_xdvx, arg_rcsn)
        if var_rgwu > 0 and arg_xdvx[var_rgwu - 1] == arg_rcsn:
            return var_rgwu - 1
        else:
            return -1
