class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_ayzf:
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = [([-1] * var_bacg) for var_wrnh in var_osiz(var_bacg)]
        return arg_ihhe.is_valid_string(0, 0, arg_xdvx, var_rgwu)

    def func_wnki(arg_ihhe, arg_egyk: var_llti, arg_dcmd: var_llti,
        arg_xdvx: var_rcsn, var_rgwu: var_zbxo[var_zbxo[var_llti]]) ->var_ayzf:
        if arg_egyk == var_hqta(arg_xdvx):
            return arg_dcmd == 0
        if var_rgwu[arg_egyk][arg_dcmd] != -1:
            return var_rgwu[arg_egyk][arg_dcmd] == 1
        var_rdmc = False
        if arg_xdvx[arg_egyk] == '*':
            var_rdmc |= arg_ihhe.is_valid_string(arg_egyk + 1, arg_dcmd + 1,
                arg_xdvx, var_rgwu)
            if arg_dcmd > 0:
                var_rdmc |= arg_ihhe.is_valid_string(arg_egyk + 1, arg_dcmd -
                    1, arg_xdvx, var_rgwu)
            var_rdmc |= arg_ihhe.is_valid_string(arg_egyk + 1, arg_dcmd,
                arg_xdvx, var_rgwu)
        elif arg_xdvx[arg_egyk] == '(':
            var_rdmc = arg_ihhe.is_valid_string(arg_egyk + 1, arg_dcmd + 1,
                arg_xdvx, var_rgwu)
        elif arg_dcmd > 0:
            var_rdmc = arg_ihhe.is_valid_string(arg_egyk + 1, arg_dcmd - 1,
                arg_xdvx, var_rgwu)
        var_rgwu[arg_egyk][arg_dcmd] = 1 if var_rdmc else 0
        return var_rdmc
