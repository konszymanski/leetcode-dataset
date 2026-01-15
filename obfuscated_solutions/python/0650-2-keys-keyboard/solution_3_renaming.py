class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = [1000] * (arg_xdvx + 1)
        var_bacg[1] = 0
        for var_hqta in var_rgwu(2, arg_xdvx + 1):
            for var_wrnh in var_rgwu(1, var_hqta // 2 + 1):
                if var_hqta % var_wrnh == 0:
                    var_bacg[var_hqta] = var_osiz(var_bacg[var_hqta], 
                        var_bacg[var_wrnh] + var_hqta // var_wrnh)
        return var_bacg[arg_xdvx]
