class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_wrnh[var_rcsn]:
        var_bacg = []
        for var_hqta in var_rgwu(1, arg_xdvx // 2 + 1):
            var_bacg.append(var_hqta)
            var_bacg.append(-var_hqta)
        if arg_xdvx % 2 == 1:
            var_bacg.append(0)
        return var_bacg
