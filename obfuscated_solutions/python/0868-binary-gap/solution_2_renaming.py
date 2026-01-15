class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = None
        var_hqta = 0
        for var_rgwu in var_wrnh(32):
            if arg_rcsn >> var_rgwu & 1:
                if var_bacg is not None:
                    var_hqta = var_osiz(var_hqta, var_rgwu - var_bacg)
                var_bacg = var_rgwu
        return var_hqta
