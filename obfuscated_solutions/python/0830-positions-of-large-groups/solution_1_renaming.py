class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = []
        var_hqta = 0
        for var_rgwu in var_wrnh(var_osiz(arg_rcsn)):
            if var_rgwu == var_osiz(arg_rcsn) - 1 or arg_rcsn[var_rgwu
                ] != arg_rcsn[var_rgwu + 1]:
                if var_rgwu - var_hqta + 1 >= 3:
                    var_bacg.append([var_hqta, var_rgwu])
                var_hqta = var_rgwu + 1
        return var_bacg
