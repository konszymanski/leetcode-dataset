class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = var_hqta = 0
        for var_rgwu in var_wrnh(var_osiz(arg_rcsn)):
            if var_rgwu and arg_rcsn[var_rgwu - 1] >= arg_rcsn[var_rgwu]:
                var_hqta = var_rgwu
            var_bacg = var_ayzf(var_bacg, var_rgwu - var_hqta + 1)
        return var_bacg
