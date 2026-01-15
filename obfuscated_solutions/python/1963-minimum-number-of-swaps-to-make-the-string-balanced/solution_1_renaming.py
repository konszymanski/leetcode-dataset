class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_osiz:
        var_bacg = var_hqta()
        var_rgwu = 0
        for var_wrnh in arg_xdvx:
            if var_wrnh == '[':
                var_bacg.append(var_wrnh)
            elif var_bacg:
                var_bacg.pop()
            else:
                var_rgwu += 1
        return (var_rgwu + 1) // 2
