class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = 0
        var_hqta = 0
        var_rgwu = 1
        while var_rgwu <= arg_xdvx:
            if arg_xdvx & var_rgwu:
                var_bacg = (1 << var_hqta + 1) - 1 - var_bacg
            var_rgwu <<= 1
            var_hqta += 1
        return var_bacg
