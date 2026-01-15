class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta = var_rgwu(arg_bacg)
        var_wrnh = [[] for var_osiz in var_ayzf(var_hqta)]
        for var_wnki, var_egyk in arg_rcsn:
            var_wrnh[var_egyk].append(var_wnki)
        var_dcmd = [None] * var_hqta

        def func_llti(arg_zbxo):
            if var_dcmd[arg_zbxo] is None:
                var_dcmd[arg_zbxo] = arg_zbxo
                for var_rdmc in var_wrnh[arg_zbxo]:
                    var_rjut = func_llti(var_rdmc)
                    if arg_bacg[var_rjut] < arg_bacg[var_dcmd[arg_zbxo]]:
                        var_dcmd[arg_zbxo] = var_rjut
            return var_dcmd[arg_zbxo]
        return var_lsgw(func_llti, var_cbvh(var_hqta))
