class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_wrnh:
        var_bacg = []
        for var_hqta in arg_xdvx:
            if not var_bacg:
                var_bacg.append(var_hqta)
                continue
            if var_hqta == 'B' and var_bacg[-1] == 'A':
                var_bacg.pop()
            elif var_hqta == 'D' and var_bacg[-1] == 'C':
                var_bacg.pop()
            else:
                var_bacg.append(var_hqta)
        return var_rgwu(var_bacg)
