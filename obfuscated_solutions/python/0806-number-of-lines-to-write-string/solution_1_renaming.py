class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta, var_rgwu = 1, 0
        for var_wrnh in arg_bacg:
            var_osiz = arg_rcsn[var_ayzf(var_wrnh) - var_ayzf('a')]
            var_rgwu += var_osiz
            if var_rgwu > 100:
                var_hqta += 1
                var_rgwu = var_osiz
        return var_hqta, var_rgwu
