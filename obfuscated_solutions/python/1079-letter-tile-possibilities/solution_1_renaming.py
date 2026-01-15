class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_osiz:
        var_bacg = var_hqta()
        var_rgwu = [False] * var_wrnh(arg_xdvx)
        arg_ihhe._generate_sequences(arg_xdvx, '', var_rgwu, var_bacg)
        return var_wrnh(var_bacg) - 1

    def func_ayzf(arg_ihhe, arg_xdvx: var_rcsn, arg_wnki: var_rcsn,
        var_rgwu: var_egyk, var_bacg: var_hqta) ->None:
        var_bacg.add(arg_wnki)
        for var_dcmd, var_llti in var_zbxo(arg_xdvx):
            if not var_rgwu[var_dcmd]:
                var_rgwu[var_dcmd] = True
                arg_ihhe._generate_sequences(arg_xdvx, arg_wnki + var_llti,
                    var_rgwu, var_bacg)
                var_rgwu[var_dcmd] = False
