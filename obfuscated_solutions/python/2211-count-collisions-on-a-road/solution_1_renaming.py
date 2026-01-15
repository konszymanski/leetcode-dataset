class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_wrnh:
        var_bacg = 0
        var_hqta = -1
        for var_rgwu in arg_xdvx:
            if var_rgwu == 'L':
                if var_hqta >= 0:
                    var_bacg += var_hqta + 1
                    var_hqta = 0
            elif var_rgwu == 'S':
                if var_hqta > 0:
                    var_bacg += var_hqta
                var_hqta = 0
            elif var_hqta >= 0:
                var_hqta += 1
            else:
                var_hqta = 1
        return var_bacg
