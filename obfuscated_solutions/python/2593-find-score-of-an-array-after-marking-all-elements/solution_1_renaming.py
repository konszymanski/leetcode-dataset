class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = 0
        var_rgwu = [(var_wrnh, var_osiz) for var_osiz, var_wrnh in var_ayzf
            (arg_xdvx)]
        var_rgwu.sort()
        var_wnki = [False] * var_egyk(arg_xdvx)
        for var_dcmd in var_llti(var_egyk(arg_xdvx)):
            var_zbxo = var_rgwu[var_dcmd][0]
            var_rdmc = var_rgwu[var_dcmd][1]
            if not var_wnki[var_rdmc]:
                var_hqta += var_zbxo
                var_wnki[var_rdmc] = True
                if var_rdmc - 1 >= 0:
                    var_wnki[var_rdmc - 1] = True
                if var_rdmc + 1 < var_egyk(arg_xdvx):
                    var_wnki[var_rdmc + 1] = True
        return var_hqta
