class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        for var_bacg in var_hqta(var_rgwu(10, var_wrnh(arg_rcsn))):
            var_osiz = arg_rcsn[:var_bacg + 1]
            if var_osiz != '0' and var_osiz.startswith('0'):
                break
            var_ayzf = var_wnki(var_osiz)
            for var_egyk in var_hqta(var_bacg + 1, var_rgwu(var_bacg + 10,
                var_wrnh(arg_rcsn))):
                var_dcmd = arg_rcsn[var_bacg + 1:var_egyk + 1]
                if var_dcmd != '0' and var_dcmd.startswith('0'):
                    break
                var_llti = var_wnki(var_dcmd)
                var_zbxo = [var_ayzf, var_llti]
                var_rdmc = var_egyk + 1
                while var_rdmc < var_wrnh(arg_rcsn):
                    var_rjut = var_zbxo[-1] + var_zbxo[-2]
                    var_lsgw = var_cbvh(var_rjut)
                    if var_rjut <= 2 ** 31 - 1 and arg_rcsn[var_rdmc:
                        ].startswith(var_lsgw):
                        var_rdmc += var_wrnh(var_lsgw)
                        var_zbxo.append(var_rjut)
                    else:
                        break
                else:
                    if var_wrnh(var_zbxo) >= 3:
                        return var_zbxo
        return []
