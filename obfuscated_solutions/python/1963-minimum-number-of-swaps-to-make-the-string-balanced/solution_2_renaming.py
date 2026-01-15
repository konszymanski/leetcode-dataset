class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rgwu:
        var_bacg = 0
        for var_hqta in arg_xdvx:
            if var_hqta == '[':
                var_bacg += 1
            elif var_bacg > 0:
                var_bacg -= 1
        return (var_bacg + 1) // 2
