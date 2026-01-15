class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rgwu:
        var_bacg = 0
        while var_bacg * var_bacg <= arg_xdvx:
            var_hqta = 0
            while var_hqta * var_hqta <= arg_xdvx:
                if var_bacg * var_bacg + var_hqta * var_hqta == arg_xdvx:
                    return True
                var_hqta += 1
            var_bacg += 1
        return False
