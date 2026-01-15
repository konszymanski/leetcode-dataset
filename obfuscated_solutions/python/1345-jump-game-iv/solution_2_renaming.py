class Solution:

    def func_udax(arg_ihhe, arg_xdvx) ->var_rjut:
        var_rcsn = var_bacg(arg_xdvx)
        if var_rcsn <= 1:
            return 0
        var_hqta = {}
        for var_rgwu in var_wrnh(var_rcsn):
            if arg_xdvx[var_rgwu] in var_hqta:
                var_hqta[arg_xdvx[var_rgwu]].append(var_rgwu)
            else:
                var_hqta[arg_xdvx[var_rgwu]] = [var_rgwu]
        var_osiz = var_ayzf([0])
        var_wnki = {0, var_rcsn - 1}
        var_egyk = 0
        var_dcmd = var_ayzf([var_rcsn - 1])
        while var_osiz:
            if var_bacg(var_osiz) > var_bacg(var_dcmd):
                var_osiz, var_dcmd = var_dcmd, var_osiz
            var_llti = var_ayzf()
            for var_zbxo in var_osiz:
                for var_rdmc in var_hqta[arg_xdvx[var_zbxo]]:
                    if var_rdmc in var_dcmd:
                        return var_egyk + 1
                    if var_rdmc not in var_wnki:
                        var_wnki.add(var_rdmc)
                        var_llti.add(var_rdmc)
                var_hqta[arg_xdvx[var_zbxo]].clear()
                for var_rdmc in [var_zbxo - 1, var_zbxo + 1]:
                    if var_rdmc in var_dcmd:
                        return var_egyk + 1
                    if 0 <= var_rdmc < var_bacg(arg_xdvx
                        ) and var_rdmc not in var_wnki:
                        var_wnki.add(var_rdmc)
                        var_llti.add(var_rdmc)
            var_osiz = var_llti
            var_egyk += 1
        return -1
