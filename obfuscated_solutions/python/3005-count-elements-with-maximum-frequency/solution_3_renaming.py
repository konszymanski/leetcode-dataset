class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = {}
        var_bacg = 0
        var_hqta = 0
        for var_rgwu in arg_xdvx:
            var_rcsn[var_rgwu] = var_rcsn.get(var_rgwu, 0) + 1
            var_wrnh = var_rcsn[var_rgwu]
            if var_wrnh > var_bacg:
                var_bacg = var_wrnh
                var_hqta = var_wrnh
            elif var_wrnh == var_bacg:
                var_hqta += var_wrnh
        return var_hqta
