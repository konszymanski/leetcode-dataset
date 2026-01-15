class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_ayzf:
        var_bacg = []
        var_hqta = []
        for var_rgwu, var_wrnh in var_osiz(arg_xdvx):
            if var_wrnh == '(':
                var_bacg.append(var_rgwu)
            elif var_wrnh == '*':
                var_hqta.append(var_rgwu)
            elif var_bacg:
                var_bacg.pop()
            elif var_hqta:
                var_hqta.pop()
            else:
                return False
        while var_bacg and var_hqta:
            if var_bacg.pop() > var_hqta.pop():
                return False
        return not var_bacg
