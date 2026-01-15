class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_osiz:
        var_bacg = arg_xdvx[0]
        var_hqta = 0
        var_rgwu = 0
        for var_wrnh in arg_xdvx:
            if var_wrnh == var_bacg:
                var_hqta += 1
                continue
            if var_hqta % 2 == 0:
                var_hqta = 1
            else:
                var_hqta = 0
                var_rgwu += 1
            var_bacg = var_wrnh
        return var_rgwu
