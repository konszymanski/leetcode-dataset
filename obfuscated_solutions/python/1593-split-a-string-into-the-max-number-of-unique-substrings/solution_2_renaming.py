class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_wrnh:
        var_bacg = var_hqta()
        var_rgwu = [0]
        arg_ihhe.backtrack(arg_xdvx, 0, var_bacg, 0, var_rgwu)
        return var_rgwu[0]

    def func_osiz(arg_ihhe, arg_xdvx: var_rcsn, arg_ayzf: var_wrnh,
        var_bacg: var_hqta, arg_wnki: var_wrnh, var_rgwu: var_egyk) ->None:
        if arg_wnki + (var_dcmd(arg_xdvx) - arg_ayzf) <= var_rgwu[0]:
            return
        if arg_ayzf == var_dcmd(arg_xdvx):
            var_rgwu[0] = var_llti(var_rgwu[0], arg_wnki)
            return
        for var_zbxo in var_rdmc(arg_ayzf + 1, var_dcmd(arg_xdvx) + 1):
            var_rjut = arg_xdvx[arg_ayzf:var_zbxo]
            if var_rjut not in var_bacg:
                var_bacg.add(var_rjut)
                arg_ihhe.backtrack(arg_xdvx, var_zbxo, var_bacg, arg_wnki +
                    1, var_rgwu)
                var_bacg.remove(var_rjut)
        return
