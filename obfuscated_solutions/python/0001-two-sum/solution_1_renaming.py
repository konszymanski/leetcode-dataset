class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_bacg[var_hqta]:
        for var_rgwu in var_wrnh(var_osiz(arg_xdvx)):
            for var_ayzf in var_wrnh(var_rgwu + 1, var_osiz(arg_xdvx)):
                if arg_xdvx[var_ayzf] == arg_rcsn - arg_xdvx[var_rgwu]:
                    return [var_rgwu, var_ayzf]
        return []
