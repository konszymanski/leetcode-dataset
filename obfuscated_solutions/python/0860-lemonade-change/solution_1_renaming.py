class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_osiz:
        var_hqta = 0
        var_rgwu = 0
        for var_wrnh in arg_xdvx:
            if var_wrnh == 5:
                var_hqta += 1
            elif var_wrnh == 10:
                if var_hqta > 0:
                    var_hqta -= 1
                    var_rgwu += 1
                else:
                    return False
            elif var_rgwu > 0 and var_hqta > 0:
                var_hqta -= 1
                var_rgwu -= 1
            elif var_hqta >= 3:
                var_hqta -= 3
            else:
                return False
        return True
