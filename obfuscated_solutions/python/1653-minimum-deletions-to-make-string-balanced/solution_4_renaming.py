class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_wrnh:
        var_bacg = []
        var_hqta = 0
        for var_rgwu in arg_xdvx:
            if var_bacg and var_bacg[-1] == 'b' and var_rgwu == 'a':
                var_bacg.pop()
                var_hqta += 1
            else:
                var_bacg.append(var_rgwu)
        return var_hqta
