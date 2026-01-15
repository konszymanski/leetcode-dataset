class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_bacg[var_hqta]:
        var_rgwu = []
        var_wrnh = []
        var_osiz = []
        for var_ayzf in arg_xdvx:
            if var_ayzf < arg_rcsn:
                var_rgwu.append(var_ayzf)
            elif var_ayzf > arg_rcsn:
                var_osiz.append(var_ayzf)
            else:
                var_wrnh.append(var_ayzf)
        var_rgwu.extend(var_wrnh)
        var_rgwu.extend(var_osiz)
        return var_rgwu
