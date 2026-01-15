class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        if arg_xdvx is None:
            return [0] * 12
        elif arg_xdvx.left is None and arg_xdvx.right is None:
            var_bacg = [0] * 12
            var_bacg[0] = 1
            return var_bacg
        var_hqta = arg_ihhe._post_order(arg_xdvx.left, arg_rcsn)
        var_rgwu = arg_ihhe._post_order(arg_xdvx.right, arg_rcsn)
        var_bacg = [0] * 12
        for var_wrnh in var_osiz(10):
            var_bacg[var_wrnh + 1] += var_hqta[var_wrnh] + var_rgwu[var_wrnh]
        var_bacg[11] = var_hqta[11] + var_rgwu[11]
        for var_ayzf in var_osiz(arg_rcsn + 1):
            for var_wnki in var_osiz(arg_rcsn + 1):
                if 2 + var_ayzf + var_wnki <= arg_rcsn:
                    var_bacg[11] += var_hqta[var_ayzf] * var_rgwu[var_wnki]
        return var_bacg

    def func_egyk(arg_ihhe, arg_dcmd: var_llti, arg_rcsn: var_zbxo) ->var_zbxo:
        return arg_ihhe._post_order(arg_dcmd, arg_rcsn)[11]
