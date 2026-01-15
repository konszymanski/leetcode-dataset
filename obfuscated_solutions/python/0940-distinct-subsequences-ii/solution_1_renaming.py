class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = [1]
        var_hqta = {}
        for var_rgwu, var_wrnh in var_osiz(arg_rcsn):
            var_bacg.append(var_bacg[-1] * 2)
            if var_wrnh in var_hqta:
                var_bacg[-1] -= var_bacg[var_hqta[var_wrnh]]
            var_hqta[var_wrnh] = var_rgwu
        return (var_bacg[-1] - 1) % (10 ** 9 + 7)
