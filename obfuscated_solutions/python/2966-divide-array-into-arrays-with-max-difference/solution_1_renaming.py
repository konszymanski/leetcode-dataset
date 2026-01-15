class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_bacg[var_bacg[var_hqta]]:
        arg_xdvx.sort()
        var_rgwu = []
        for var_wrnh in var_osiz(0, var_ayzf(arg_xdvx), 3):
            if arg_xdvx[var_wrnh + 2] - arg_xdvx[var_wrnh] > arg_rcsn:
                return []
            var_rgwu.append([arg_xdvx[var_wrnh], arg_xdvx[var_wrnh + 1],
                arg_xdvx[var_wrnh + 2]])
        return var_rgwu
