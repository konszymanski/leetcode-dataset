class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = 0
        var_rgwu = var_wrnh(arg_xdvx)
        for var_osiz in var_ayzf(var_rgwu):
            var_wnki = arg_xdvx[var_osiz]
            for var_egyk in var_ayzf(var_rgwu):
                var_dcmd = arg_xdvx[var_egyk]
                if var_osiz == var_egyk or not (var_wnki[0] <= var_dcmd[0] and
                    var_wnki[1] >= var_dcmd[1]):
                    continue
                if var_rgwu == 2:
                    var_hqta += 1
                    continue
                var_llti = False
                for var_zbxo in var_ayzf(var_rgwu):
                    if var_zbxo == var_osiz or var_zbxo == var_egyk:
                        continue
                    var_rdmc = arg_xdvx[var_zbxo]
                    var_rjut = var_rdmc[0] >= var_wnki[0] and var_rdmc[0
                        ] <= var_dcmd[0]
                    var_lsgw = var_rdmc[1] <= var_wnki[1] and var_rdmc[1
                        ] >= var_dcmd[1]
                    if var_rjut and var_lsgw:
                        var_llti = True
                        break
                if not var_llti:
                    var_hqta += 1
        return var_hqta
