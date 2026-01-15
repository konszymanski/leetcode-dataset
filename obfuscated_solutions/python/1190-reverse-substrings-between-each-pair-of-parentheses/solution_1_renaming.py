class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = var_hqta()
        var_rgwu = []
        for var_wrnh in arg_xdvx:
            if var_wrnh == '(':
                var_bacg.append(var_osiz(var_rgwu))
            elif var_wrnh == ')':
                var_ayzf = var_bacg.pop()
                var_rgwu[var_ayzf:] = var_rgwu[var_ayzf:][::-1]
            else:
                var_rgwu.append(var_wrnh)
        return ''.join(var_rgwu)
