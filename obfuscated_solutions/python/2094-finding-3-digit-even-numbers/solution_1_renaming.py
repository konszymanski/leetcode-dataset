class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        var_hqta = var_rgwu()
        var_wrnh = var_osiz(arg_xdvx)
        for var_ayzf in var_wnki(var_wrnh):
            for var_egyk in var_wnki(var_wrnh):
                for var_dcmd in var_wnki(var_wrnh):
                    if (var_ayzf == var_egyk or var_egyk == var_dcmd or 
                        var_ayzf == var_dcmd):
                        continue
                    var_llti = arg_xdvx[var_ayzf] * 100 + arg_xdvx[var_egyk
                        ] * 10 + arg_xdvx[var_dcmd]
                    if var_llti >= 100 and var_llti % 2 == 0:
                        var_hqta.add(var_llti)
        var_zbxo = var_rdmc(var_rjut(var_hqta))
        return var_zbxo
