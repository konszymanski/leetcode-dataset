class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = 0
        var_hqta = 1
        while arg_xdvx > 0:
            for var_rgwu in var_wrnh(var_osiz(arg_xdvx, 7)):
                var_bacg += var_hqta + var_rgwu
            arg_xdvx -= 7
            var_hqta += 1
        return var_bacg
