class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = []
        for var_bacg in arg_xdvx:
            var_rcsn.append([var_bacg[0], 1, var_bacg[2]])
            var_rcsn.append([var_bacg[1] + 1, 0, var_bacg[2]])
        var_hqta, var_rgwu = 0, 0
        var_rcsn.sort()
        for var_wrnh in var_rcsn:
            if var_wrnh[1]:
                var_hqta = var_osiz(var_hqta, var_wrnh[2] + var_rgwu)
            else:
                var_rgwu = var_osiz(var_rgwu, var_wrnh[2])
        return var_hqta
