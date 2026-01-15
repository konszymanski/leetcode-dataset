class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = 0
        var_bacg = 0
        var_hqta = 0
        for var_rgwu in arg_xdvx:
            var_hqta += var_rgwu
            var_rcsn = var_wrnh(var_rcsn, var_hqta)
            var_bacg = var_osiz(var_bacg, var_hqta)
        return var_bacg - var_rcsn
