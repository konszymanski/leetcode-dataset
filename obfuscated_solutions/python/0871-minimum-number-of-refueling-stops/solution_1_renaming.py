class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg, arg_hqta):
        var_rgwu = [arg_bacg] + [0] * var_wrnh(arg_hqta)
        for var_osiz, (var_ayzf, var_wnki) in var_egyk(arg_hqta):
            for var_dcmd in var_llti(var_osiz, -1, -1):
                if var_rgwu[var_dcmd] >= var_ayzf:
                    var_rgwu[var_dcmd + 1] = var_zbxo(var_rgwu[var_dcmd + 1
                        ], var_rgwu[var_dcmd] + var_wnki)
        for var_osiz, var_rdmc in var_egyk(var_rgwu):
            if var_rdmc >= arg_rcsn:
                return var_osiz
        return -1
